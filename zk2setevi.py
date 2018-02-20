from zkutils import *
import os
from collections import defaultdict
import markdown as md
import json


class Zk2Setevi:
    def __init__(self, home=None, folder=None, extension='.md', linkstyle='double'):
        if home is None:
            raise RuntimeError('no home')
        if folder is None:
            raise RuntimeError('no folder')
        self.home = home
        self.folder = folder
        self.extension = extension
        self.linkstyle = linkstyle

        if linkstyle not in ['single', 'double', '§']:
            linkstyle = 'double'
        if linkstyle == 'double':
            self.link_prefix = '[['
            self.link_postfix = ']]'
        elif linkstyle == 'single':
            self.link_prefix = '[['
            self.link_postfix = ']]'
        else:
            self.link_prefix = '§'
            self.link_postfix = ''
        self.note_tags = {}
        self.tag_notes = defaultdict(set)
        self.note_titles = {}
        self.json_note_ids = {}
        self.json_tag_ids = {}
        self.json_id_counter = -1
        self.json_nodes = []

    def next_id(self):
        self.json_id_counter += 1
        return self.json_id_counter

    def get_all_notes(self):
        """
        Return all files with extension in folder.
        """
        candidates = []
        for root, dirs, files in os.walk(self.folder):
            candidates.extend([f for f in files if f.endswith(self.extension)])
        return candidates

    def find_all_notes_all_tags(self):
        """
        Manual implementation to get a dict mapping note_ids to tags
        and tags to note ids. Also record note titles
        """
        # manual implementation
        for filn in self.get_all_notes():
            note_id = self.get_note_id_of_file(filn)
            if not note_id:
                continue
            _, title = filn.split(' ', 1)
            title = title.replace(self.extension, '')
            self.note_titles[note_id] = title
            tags = list(self.extract_tags(filn))

            if tags:
                self.note_tags[note_id] = tags
                for tag in tags:
                    self.tag_notes[tag].add(note_id)

    @staticmethod
    def cut_after_note_id(text):
        """
        Tries to find the 12/14 digit note ID (at beginning) in text.
        """
        note_ids = re.findall('[0-9.]{12,18}', text)
        if note_ids:
            return note_ids[0]

    def get_note_id_of_file(self, filn):
        """
        Return the note id of the file named filn or None.
        """
        if filn.endswith(self.extension):
            # we have a markdown file
            note_id = self.cut_after_note_id(os.path.basename(filn))
            if note_id:
                if os.path.basename(filn).startswith(note_id):
                    return note_id

    def note_file_by_id(self, note_id):
        """
        Find the file for note_id.
        """
        if not note_id:
            return
        candidates = []
        for root, dirs, files in os.walk(self.folder):
            candidates.extend([os.path.join(root, f) for f in files if f.startswith(note_id)])
        if len(candidates) > 0:
            return candidates[0]

    def extract_tags(self, file):
        """
        Extract #tags from file.
        Returns all words starting with `#`.
        To be precise, it returns everything that matches RE_TAGS_PY.
        """
        tags = set()
        full_p = os.path.join(self.folder, file)
        with open(full_p, mode='r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                for tag in re.findall(ZkConstants.RE_TAGS_PY, line):
                    tags.add(tag[0])
        return tags

    def enumerate_items(self):
        """
        Enumerate note ids and tags (and citekeys).
        """
        for noteid in sorted(self.note_titles.keys()):
            self.json_note_ids[noteid] = self.next_id()
        for tag in sorted(self.tag_notes.keys()):
            self.json_tag_ids[tag] = self.next_id()

    def create_nodes_from_note(self, noteid):
        filn = self.note_file_by_id(note_id=noteid)
        if not filn:
            return None
        node_id = self.json_note_ids[noteid]

        filn = os.path.join(self.folder, filn)
        with open(filn, mode='r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        chunk_rel_ids = []
        current_chunk = ''
        for line in lines:
            has_links = ZkConstants.Link_Matcher.search(line)
            if not has_links:
                current_chunk += line + '\n'
            else:
                # split line into chunks
                # terminate current chunk with text before link
                note_id_expected = False
                for item in ZkConstants.Link_Matcher.split(line):
                    if item is None:
                        continue
                    if item.startswith('[') or item.startswith('§'):
                        note_id_expected = True
                        continue
                    if item.startswith(']'):
                        continue
                    if note_id_expected:
                        # finalize current chunk
                        chunk_id = self.create_text_node(current_chunk)
                        chunk_rel_ids.append(self.create_relationship_node(node_id, chunk_id))
                        note_id_expected = False
                        current_chunk = ''
                        # now process link
                        rel_id, chunk_id = self.create_note_link_node(item)
                        chunk_rel_ids.append(rel_id)
                    else:
                        current_chunk += item
        if current_chunk:
            chunk_id = self.create_text_node(current_chunk)
            chunk_rel_ids.append(self.create_relationship_node(node_id, chunk_id))
        # embed the chunks into a note node
        self.json_nodes.append({
            'dataNodeId': node_id,
            'name': self.note_titles[noteid],
            'classAttr': 'SimpleDataNode',
            'relationships': chunk_rel_ids
        })

    def create_text_node(self, text):
        node_id = self.next_id()
        self.json_nodes.append({
            'dataNodeId': node_id,
            'name': md.markdown(text),
            'classAttr': 'SimpleDataNode',
            'relationships': []
        })
        return node_id

    def create_note_link_node(self, to_noteid):
        node_id = self.next_id()
        to_id = self.json_note_ids[to_noteid]
        rel_id = self.create_relationship_node(node_id, to_id)
        link_text = '{}{}{} {}'.format(self.link_prefix, to_noteid,
                                       self.link_postfix,
                                       self.note_titles[to_noteid])
        self.json_nodes.append({
            'dataNodeId': node_id,
            'name': link_text,
            'classAttr': 'SimpleDataNode',
            'relationships': [rel_id]
        })
        return rel_id, node_id

    def create_relationship_node(self, from_id, to_id):
        node_id = self.next_id()
        self.json_nodes.append({
            'dataNodeId': node_id,
            'classAttr': 'HasDetail',
            'from': from_id,
            'to': to_id
        })
        return node_id

    def create_all_tags_node(self):
        # also create all tag notes
        node_id = self.next_id()
        rel_ids = []
        for tag in sorted(self.tag_notes.keys()):
            note_ids = self.tag_notes[tag]
            tag_node = self.json_tag_ids[tag]
            tag_rel_ids = []
            for note_id in note_ids:
                rel_id = self.create_relationship_node(tag_node, self.json_note_ids[note_id])
                tag_rel_ids.append(rel_id)
            self.json_nodes.append({
                'dataNodeId': tag_node,
                'name': tag,
                'classAttr': 'SimpleDataNode',
                'relationships': tag_rel_ids
            })
            rel_id = self.create_relationship_node(node_id, tag_node)
            rel_ids.append(rel_id)
        self.json_nodes.append({
            'dataNodeId': node_id,
            'name': '#tags',
            'classAttr': 'SimpleDataNode',
            'relationships': rel_ids
        })
        return node_id

    def create_all_notes_node(self):
        json_note_ids = sorted(list(self.json_note_ids.keys()))
        node_id = self.next_id()
        rel_node_ids = []
        for note_id in json_note_ids:
            rel_id, _ = self.create_note_link_node(note_id)
            rel_node_ids.append(rel_id)
        self.json_nodes.append({
            'dataNodeId': node_id,
            'name': 'notes',
            'classAttr': 'SimpleDataNode',
            'relationships': rel_node_ids
        })
        return node_id

    def create_root_node(self):
        n_id = self.create_all_notes_node()
        t_id = self.create_all_tags_node()
        root_id = self.next_id()
        rel_ids = [self.create_relationship_node(root_id, t_id),
                   self.create_relationship_node(root_id, n_id)]
        self.json_nodes.append({
            'dataNodeId': root_id,
            'name': 'Zettelkasten',
            'classAttr': 'SimpleDataNode',
            'relationships': rel_ids
        })
        return root_id

    def create_all_nodes(self):
        for note_id in sorted(self.note_titles.keys()):
            self.create_nodes_from_note(note_id)

        root_id = self.create_root_node()
        return root_id

    def create_json(self):
        root_id = self.create_all_nodes()
        json_dict = {
            'listOfAllDataNodes': self.json_nodes,
            'rootNode': root_id
        }
        json_s = json.dumps(json_dict)
        with open(os.path.join(self.home, 'output', 'out.json'), mode='w', encoding='utf-8') as f:
            f.write(json_s)
        return json_s

    def create_html(self):
        self.find_all_notes_all_tags()
        self.enumerate_items()
        json_s = self.create_json()
        with open(os.path.join(self.home, 'data', 'template-default.html'), mode='r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        output_lines = []
        for line in lines:
            if '/*GENERATED JSON*/' in line:
                line = line.replace('/*GENERATED JSON*/', json_s)
            output_lines.append(line)

        with open(os.path.join(self.home, 'output', 'out.html'), mode='w', encoding='utf-8') as f:
            for line in output_lines:
                f.write(line + '\n')


if __name__ == '__main__':
    print('ZK to Setevi')
    home = os.path.dirname(os.path.abspath(__file__))
    zk_folder = os.path.join(home, 'scratch', 'zksetevi')
    print(home)

    z = Zk2Setevi(home=home, folder=zk_folder)
    z.create_html()

