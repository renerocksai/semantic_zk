from cx_Freeze import setup,Executable
import os
import sys



includes = ["atexit","PyQt5.QtCore", "PyQt5.Qt", "PyQt5.QtGui", "PyQt5.QtWidgets",
            "pygments",
"pygments.lexers.actionscript.py","pygments.lexers.agile.py","pygments.lexers.algebra.py","pygments.lexers.ambient.py","pygments.lexers.ampl.py","pygments.lexers.apl.py","pygments.lexers.archetype.py","pygments.lexers.asm.py","pygments.lexers.automation.py","pygments.lexers.basic.py","pygments.lexers.bibtex.py","pygments.lexers.business.py","pygments.lexers.c_cpp.py","pygments.lexers.c_like.py","pygments.lexers.capnproto.py","pygments.lexers.chapel.py","pygments.lexers.clean.py","pygments.lexers.compiled.py","pygments.lexers.configs.py","pygments.lexers.console.py","pygments.lexers.crystal.py","pygments.lexers.csound.py","pygments.lexers.css.py","pygments.lexers.d.py","pygments.lexers.dalvik.py","pygments.lexers.data.py","pygments.lexers.diff.py","pygments.lexers.dotnet.py","pygments.lexers.dsls.py","pygments.lexers.dylan.py","pygments.lexers.ecl.py","pygments.lexers.eiffel.py","pygments.lexers.elm.py","pygments.lexers.erlang.py","pygments.lexers.esoteric.py","pygments.lexers.ezhil.py","pygments.lexers.factor.py","pygments.lexers.fantom.py","pygments.lexers.felix.py","pygments.lexers.forth.py","pygments.lexers.fortran.py","pygments.lexers.foxpro.py","pygments.lexers.functional.py","pygments.lexers.go.py","pygments.lexers.grammar_notation.py","pygments.lexers.graph.py","pygments.lexers.graphics.py","pygments.lexers.haskell.py","pygments.lexers.haxe.py","pygments.lexers.hdl.py","pygments.lexers.hexdump.py","pygments.lexers.html.py","pygments.lexers.idl.py","pygments.lexers.igor.py","pygments.lexers.inferno.py","pygments.lexers.installers.py","pygments.lexers.int_fiction.py","pygments.lexers.iolang.py","pygments.lexers.j.py","pygments.lexers.javascript.py","pygments.lexers.julia.py","pygments.lexers.jvm.py","pygments.lexers.lisp.py","pygments.lexers.make.py","pygments.lexers.markup.py","pygments.lexers.math.py","pygments.lexers.matlab.py","pygments.lexers.ml.py","pygments.lexers.modeling.py","pygments.lexers.modula2.py","pygments.lexers.monte.py","pygments.lexers.ncl.py","pygments.lexers.nimrod.py","pygments.lexers.nit.py","pygments.lexers.nix.py","pygments.lexers.oberon.py","pygments.lexers.objective.py","pygments.lexers.ooc.py","pygments.lexers.other.py","pygments.lexers.parasail.py","pygments.lexers.parsers.py","pygments.lexers.pascal.py","pygments.lexers.pawn.py","pygments.lexers.perl.py","pygments.lexers.php.py","pygments.lexers.praat.py","pygments.lexers.prolog.py","pygments.lexers.python.py","pygments.lexers.qvt.py","pygments.lexers.r.py","pygments.lexers.rdf.py","pygments.lexers.rebol.py","pygments.lexers.resource.py","pygments.lexers.rnc.py","pygments.lexers.roboconf.py","pygments.lexers.robotframework.py","pygments.lexers.ruby.py","pygments.lexers.rust.py","pygments.lexers.sas.py","pygments.lexers.scripting.py","pygments.lexers.shell.py","pygments.lexers.smalltalk.py","pygments.lexers.smv.py","pygments.lexers.snobol.py","pygments.lexers.special.py","pygments.lexers.sql.py","pygments.lexers.stata.py","pygments.lexers.supercollider.py","pygments.lexers.tcl.py","pygments.lexers.templates.py","pygments.lexers.testing.py","pygments.lexers.text.py","pygments.lexers.textedit.py","pygments.lexers.textfmts.py","pygments.lexers.theorem.py","pygments.lexers.trafficscript.py","pygments.lexers.typoscript.py","pygments.lexers.urbi.py","pygments.lexers.varnish.py","pygments.lexers.verification.py","pygments.lexers.web.py","pygments.lexers.webmisc.py","pygments.lexers.whiley.py","pygments.lexers.x10.py",            ]
includefiles = [('data/setevi-template.html', 'data/setevi-template.html')]  #path_platforms
excludes = [
    '_gtkagg', '_tkagg', 'bsddb', 'curses', 'pywin.debugger',
    'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
    'Tkconstants', 'Tkinter', 'scipy', "numpy", "numpy.core"
]
packages = ["os", ]
path = []

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
                     "includes":      includes,
                     "include_files": includefiles,
                     "excludes":      excludes,
                     "packages":      packages,
                     "path":          path
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
exe = None

semantic_zk = Executable(
      script="semantic_zk.py",
      initScript = None,
    )

zk2setevi = Executable(
      script="zk2setevi.py",
      initScript = None,
    )

setup(
      name = "semantic_zk",
      version = "0.1",
      author = 'me',
      description = "My GUI application!",
      options = {"build_exe": build_exe_options},
      executables = [zk2setevi, semantic_zk]
)
