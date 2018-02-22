template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SeTeVi</title>
    <style>
        p {
            margin: 0px;
            padding: 0px;
        }
    </style>
</head>
<body>
<script>

/** vim: et:ts=4:sw=4:sts=4
 * @license RequireJS 2.3.3 Copyright jQuery Foundation and other contributors.
 * Released under MIT license, https://github.com/requirejs/requirejs/blob/master/LICENSE
 */
var requirejs,require,define;!function(global,setTimeout){function commentReplace(e,t){return t||""}function isFunction(e){return"[object Function]"===ostring.call(e)}function isArray(e){return"[object Array]"===ostring.call(e)}function each(e,t){if(e){var i;for(i=0;i<e.length&&(!e[i]||!t(e[i],i,e));i+=1);}}function eachReverse(e,t){if(e){var i;for(i=e.length-1;i>-1&&(!e[i]||!t(e[i],i,e));i-=1);}}function hasProp(e,t){return hasOwn.call(e,t)}function getOwn(e,t){return hasProp(e,t)&&e[t]}function eachProp(e,t){var i;for(i in e)if(hasProp(e,i)&&t(e[i],i))break}function mixin(e,t,i,r){return t&&eachProp(t,function(t,n){!i&&hasProp(e,n)||(!r||"object"!=typeof t||!t||isArray(t)||isFunction(t)||t instanceof RegExp?e[n]=t:(e[n]||(e[n]={}),mixin(e[n],t,i,r)))}),e}function bind(e,t){return function(){return t.apply(e,arguments)}}function scripts(){return document.getElementsByTagName("script")}function defaultOnError(e){throw e}function getGlobal(e){if(!e)return e;var t=global;return each(e.split("."),function(e){t=t[e]}),t}function makeError(e,t,i,r){var n=new Error(t+"\nhttp://requirejs.org/docs/errors.html#"+e);return n.requireType=e,n.requireModules=r,i&&(n.originalError=i),n}function newContext(e){function t(e){var t,i;for(t=0;t<e.length;t++)if(i=e[t],"."===i)e.splice(t,1),t-=1;else if(".."===i){if(0===t||1===t&&".."===e[2]||".."===e[t-1])continue;t>0&&(e.splice(t-1,2),t-=2)}}function i(e,i,r){var n,o,a,s,u,c,d,p,f,l,h,m,g=i&&i.split("/"),v=y.map,x=v&&v["*"];if(e&&(e=e.split("/"),d=e.length-1,y.nodeIdCompat&&jsSuffixRegExp.test(e[d])&&(e[d]=e[d].replace(jsSuffixRegExp,"")),"."===e[0].charAt(0)&&g&&(m=g.slice(0,g.length-1),e=m.concat(e)),t(e),e=e.join("/")),r&&v&&(g||x)){a=e.split("/");e:for(s=a.length;s>0;s-=1){if(c=a.slice(0,s).join("/"),g)for(u=g.length;u>0;u-=1)if(o=getOwn(v,g.slice(0,u).join("/")),o&&(o=getOwn(o,c))){p=o,f=s;break e}!l&&x&&getOwn(x,c)&&(l=getOwn(x,c),h=s)}!p&&l&&(p=l,f=h),p&&(a.splice(0,f,p),e=a.join("/"))}return n=getOwn(y.pkgs,e),n?n:e}function r(e){isBrowser&&each(scripts(),function(t){if(t.getAttribute("data-requiremodule")===e&&t.getAttribute("data-requirecontext")===q.contextName)return t.parentNode.removeChild(t),!0})}function n(e){var t=getOwn(y.paths,e);if(t&&isArray(t)&&t.length>1)return t.shift(),q.require.undef(e),q.makeRequire(null,{skipMap:!0})([e]),!0}function o(e){var t,i=e?e.indexOf("!"):-1;return i>-1&&(t=e.substring(0,i),e=e.substring(i+1,e.length)),[t,e]}function a(e,t,r,n){var a,s,u,c,d=null,p=t?t.name:null,f=e,l=!0,h="";return e||(l=!1,e="_@r"+(T+=1)),c=o(e),d=c[0],e=c[1],d&&(d=i(d,p,n),s=getOwn(j,d)),e&&(d?h=r?e:s&&s.normalize?s.normalize(e,function(e){return i(e,p,n)}):e.indexOf("!")===-1?i(e,p,n):e:(h=i(e,p,n),c=o(h),d=c[0],h=c[1],r=!0,a=q.nameToUrl(h))),u=!d||s||r?"":"_unnormalized"+(A+=1),{prefix:d,name:h,parentMap:t,unnormalized:!!u,url:a,originalName:f,isDefine:l,id:(d?d+"!"+h:h)+u}}function s(e){var t=e.id,i=getOwn(S,t);return i||(i=S[t]=new q.Module(e)),i}function u(e,t,i){var r=e.id,n=getOwn(S,r);!hasProp(j,r)||n&&!n.defineEmitComplete?(n=s(e),n.error&&"error"===t?i(n.error):n.on(t,i)):"defined"===t&&i(j[r])}function c(e,t){var i=e.requireModules,r=!1;t?t(e):(each(i,function(t){var i=getOwn(S,t);i&&(i.error=e,i.events.error&&(r=!0,i.emit("error",e)))}),r||req.onError(e))}function d(){globalDefQueue.length&&(each(globalDefQueue,function(e){var t=e[0];"string"==typeof t&&(q.defQueueMap[t]=!0),O.push(e)}),globalDefQueue=[])}function p(e){delete S[e],delete k[e]}function f(e,t,i){var r=e.map.id;e.error?e.emit("error",e.error):(t[r]=!0,each(e.depMaps,function(r,n){var o=r.id,a=getOwn(S,o);!a||e.depMatched[n]||i[o]||(getOwn(t,o)?(e.defineDep(n,j[o]),e.check()):f(a,t,i))}),i[r]=!0)}function l(){var e,t,i=1e3*y.waitSeconds,o=i&&q.startTime+i<(new Date).getTime(),a=[],s=[],u=!1,d=!0;if(!x){if(x=!0,eachProp(k,function(e){var i=e.map,c=i.id;if(e.enabled&&(i.isDefine||s.push(e),!e.error))if(!e.inited&&o)n(c)?(t=!0,u=!0):(a.push(c),r(c));else if(!e.inited&&e.fetched&&i.isDefine&&(u=!0,!i.prefix))return d=!1}),o&&a.length)return e=makeError("timeout","Load timeout for modules: "+a,null,a),e.contextName=q.contextName,c(e);d&&each(s,function(e){f(e,{},{})}),o&&!t||!u||!isBrowser&&!isWebWorker||w||(w=setTimeout(function(){w=0,l()},50)),x=!1}}function h(e){hasProp(j,e[0])||s(a(e[0],null,!0)).init(e[1],e[2])}function m(e,t,i,r){e.detachEvent&&!isOpera?r&&e.detachEvent(r,t):e.removeEventListener(i,t,!1)}function g(e){var t=e.currentTarget||e.srcElement;return m(t,q.onScriptLoad,"load","onreadystatechange"),m(t,q.onScriptError,"error"),{node:t,id:t&&t.getAttribute("data-requiremodule")}}function v(){var e;for(d();O.length;){if(e=O.shift(),null===e[0])return c(makeError("mismatch","Mismatched anonymous define() module: "+e[e.length-1]));h(e)}q.defQueueMap={}}var x,b,q,E,w,y={waitSeconds:7,baseUrl:"./",paths:{},bundles:{},pkgs:{},shim:{},config:{}},S={},k={},M={},O=[],j={},P={},R={},T=1,A=1;return E={require:function(e){return e.require?e.require:e.require=q.makeRequire(e.map)},exports:function(e){if(e.usingExports=!0,e.map.isDefine)return e.exports?j[e.map.id]=e.exports:e.exports=j[e.map.id]={}},module:function(e){return e.module?e.module:e.module={id:e.map.id,uri:e.map.url,config:function(){return getOwn(y.config,e.map.id)||{}},exports:e.exports||(e.exports={})}}},b=function(e){this.events=getOwn(M,e.id)||{},this.map=e,this.shim=getOwn(y.shim,e.id),this.depExports=[],this.depMaps=[],this.depMatched=[],this.pluginMaps={},this.depCount=0},b.prototype={init:function(e,t,i,r){r=r||{},this.inited||(this.factory=t,i?this.on("error",i):this.events.error&&(i=bind(this,function(e){this.emit("error",e)})),this.depMaps=e&&e.slice(0),this.errback=i,this.inited=!0,this.ignore=r.ignore,r.enabled||this.enabled?this.enable():this.check())},defineDep:function(e,t){this.depMatched[e]||(this.depMatched[e]=!0,this.depCount-=1,this.depExports[e]=t)},fetch:function(){if(!this.fetched){this.fetched=!0,q.startTime=(new Date).getTime();var e=this.map;return this.shim?void q.makeRequire(this.map,{enableBuildCallback:!0})(this.shim.deps||[],bind(this,function(){return e.prefix?this.callPlugin():this.load()})):e.prefix?this.callPlugin():this.load()}},load:function(){var e=this.map.url;P[e]||(P[e]=!0,q.load(this.map.id,e))},check:function(){if(this.enabled&&!this.enabling){var e,t,i=this.map.id,r=this.depExports,n=this.exports,o=this.factory;if(this.inited){if(this.error)this.emit("error",this.error);else if(!this.defining){if(this.defining=!0,this.depCount<1&&!this.defined){if(isFunction(o)){if(this.events.error&&this.map.isDefine||req.onError!==defaultOnError)try{n=q.execCb(i,o,r,n)}catch(t){e=t}else n=q.execCb(i,o,r,n);if(this.map.isDefine&&void 0===n&&(t=this.module,t?n=t.exports:this.usingExports&&(n=this.exports)),e)return e.requireMap=this.map,e.requireModules=this.map.isDefine?[this.map.id]:null,e.requireType=this.map.isDefine?"define":"require",c(this.error=e)}else n=o;if(this.exports=n,this.map.isDefine&&!this.ignore&&(j[i]=n,req.onResourceLoad)){var a=[];each(this.depMaps,function(e){a.push(e.normalizedMap||e)}),req.onResourceLoad(q,this.map,a)}p(i),this.defined=!0}this.defining=!1,this.defined&&!this.defineEmitted&&(this.defineEmitted=!0,this.emit("defined",this.exports),this.defineEmitComplete=!0)}}else hasProp(q.defQueueMap,i)||this.fetch()}},callPlugin:function(){var e=this.map,t=e.id,r=a(e.prefix);this.depMaps.push(r),u(r,"defined",bind(this,function(r){var n,o,d,f=getOwn(R,this.map.id),l=this.map.name,h=this.map.parentMap?this.map.parentMap.name:null,m=q.makeRequire(e.parentMap,{enableBuildCallback:!0});return this.map.unnormalized?(r.normalize&&(l=r.normalize(l,function(e){return i(e,h,!0)})||""),o=a(e.prefix+"!"+l,this.map.parentMap,!0),u(o,"defined",bind(this,function(e){this.map.normalizedMap=o,this.init([],function(){return e},null,{enabled:!0,ignore:!0})})),d=getOwn(S,o.id),void(d&&(this.depMaps.push(o),this.events.error&&d.on("error",bind(this,function(e){this.emit("error",e)})),d.enable()))):f?(this.map.url=q.nameToUrl(f),void this.load()):(n=bind(this,function(e){this.init([],function(){return e},null,{enabled:!0})}),n.error=bind(this,function(e){this.inited=!0,this.error=e,e.requireModules=[t],eachProp(S,function(e){0===e.map.id.indexOf(t+"_unnormalized")&&p(e.map.id)}),c(e)}),n.fromText=bind(this,function(i,r){var o=e.name,u=a(o),d=useInteractive;r&&(i=r),d&&(useInteractive=!1),s(u),hasProp(y.config,t)&&(y.config[o]=y.config[t]);try{req.exec(i)}catch(e){return c(makeError("fromtexteval","fromText eval for "+t+" failed: "+e,e,[t]))}d&&(useInteractive=!0),this.depMaps.push(u),q.completeLoad(o),m([o],n)}),void r.load(e.name,m,n,y))})),q.enable(r,this),this.pluginMaps[r.id]=r},enable:function(){k[this.map.id]=this,this.enabled=!0,this.enabling=!0,each(this.depMaps,bind(this,function(e,t){var i,r,n;if("string"==typeof e){if(e=a(e,this.map.isDefine?this.map:this.map.parentMap,!1,!this.skipMap),this.depMaps[t]=e,n=getOwn(E,e.id))return void(this.depExports[t]=n(this));this.depCount+=1,u(e,"defined",bind(this,function(e){this.undefed||(this.defineDep(t,e),this.check())})),this.errback?u(e,"error",bind(this,this.errback)):this.events.error&&u(e,"error",bind(this,function(e){this.emit("error",e)}))}i=e.id,r=S[i],hasProp(E,i)||!r||r.enabled||q.enable(e,this)})),eachProp(this.pluginMaps,bind(this,function(e){var t=getOwn(S,e.id);t&&!t.enabled&&q.enable(e,this)})),this.enabling=!1,this.check()},on:function(e,t){var i=this.events[e];i||(i=this.events[e]=[]),i.push(t)},emit:function(e,t){each(this.events[e],function(e){e(t)}),"error"===e&&delete this.events[e]}},q={config:y,contextName:e,registry:S,defined:j,urlFetched:P,defQueue:O,defQueueMap:{},Module:b,makeModuleMap:a,nextTick:req.nextTick,onError:c,configure:function(e){if(e.baseUrl&&"/"!==e.baseUrl.charAt(e.baseUrl.length-1)&&(e.baseUrl+="/"),"string"==typeof e.urlArgs){var t=e.urlArgs;e.urlArgs=function(e,i){return(i.indexOf("?")===-1?"?":"&")+t}}var i=y.shim,r={paths:!0,bundles:!0,config:!0,map:!0};eachProp(e,function(e,t){r[t]?(y[t]||(y[t]={}),mixin(y[t],e,!0,!0)):y[t]=e}),e.bundles&&eachProp(e.bundles,function(e,t){each(e,function(e){e!==t&&(R[e]=t)})}),e.shim&&(eachProp(e.shim,function(e,t){isArray(e)&&(e={deps:e}),!e.exports&&!e.init||e.exportsFn||(e.exportsFn=q.makeShimExports(e)),i[t]=e}),y.shim=i),e.packages&&each(e.packages,function(e){var t,i;e="string"==typeof e?{name:e}:e,i=e.name,t=e.location,t&&(y.paths[i]=e.location),y.pkgs[i]=e.name+"/"+(e.main||"main").replace(currDirRegExp,"").replace(jsSuffixRegExp,"")}),eachProp(S,function(e,t){e.inited||e.map.unnormalized||(e.map=a(t,null,!0))}),(e.deps||e.callback)&&q.require(e.deps||[],e.callback)},makeShimExports:function(e){function t(){var t;return e.init&&(t=e.init.apply(global,arguments)),t||e.exports&&getGlobal(e.exports)}return t},makeRequire:function(t,n){function o(i,r,u){var d,p,f;return n.enableBuildCallback&&r&&isFunction(r)&&(r.__requireJsBuild=!0),"string"==typeof i?isFunction(r)?c(makeError("requireargs","Invalid require call"),u):t&&hasProp(E,i)?E[i](S[t.id]):req.get?req.get(q,i,t,o):(p=a(i,t,!1,!0),d=p.id,hasProp(j,d)?j[d]:c(makeError("notloaded",'Module name "'+d+'" has not been loaded yet for context: '+e+(t?"":". Use require([])")))):(v(),q.nextTick(function(){v(),f=s(a(null,t)),f.skipMap=n.skipMap,f.init(i,r,u,{enabled:!0}),l()}),o)}return n=n||{},mixin(o,{isBrowser:isBrowser,toUrl:function(e){var r,n=e.lastIndexOf("."),o=e.split("/")[0],a="."===o||".."===o;return n!==-1&&(!a||n>1)&&(r=e.substring(n,e.length),e=e.substring(0,n)),q.nameToUrl(i(e,t&&t.id,!0),r,!0)},defined:function(e){return hasProp(j,a(e,t,!1,!0).id)},specified:function(e){return e=a(e,t,!1,!0).id,hasProp(j,e)||hasProp(S,e)}}),t||(o.undef=function(e){d();var i=a(e,t,!0),n=getOwn(S,e);n.undefed=!0,r(e),delete j[e],delete P[i.url],delete M[e],eachReverse(O,function(t,i){t[0]===e&&O.splice(i,1)}),delete q.defQueueMap[e],n&&(n.events.defined&&(M[e]=n.events),p(e))}),o},enable:function(e){var t=getOwn(S,e.id);t&&s(e).enable()},completeLoad:function(e){var t,i,r,o=getOwn(y.shim,e)||{},a=o.exports;for(d();O.length;){if(i=O.shift(),null===i[0]){if(i[0]=e,t)break;t=!0}else i[0]===e&&(t=!0);h(i)}if(q.defQueueMap={},r=getOwn(S,e),!t&&!hasProp(j,e)&&r&&!r.inited){if(!(!y.enforceDefine||a&&getGlobal(a)))return n(e)?void 0:c(makeError("nodefine","No define call for "+e,null,[e]));h([e,o.deps||[],o.exportsFn])}l()},nameToUrl:function(e,t,i){var r,n,o,a,s,u,c,d=getOwn(y.pkgs,e);if(d&&(e=d),c=getOwn(R,e))return q.nameToUrl(c,t,i);if(req.jsExtRegExp.test(e))s=e+(t||"");else{for(r=y.paths,n=e.split("/"),o=n.length;o>0;o-=1)if(a=n.slice(0,o).join("/"),u=getOwn(r,a)){isArray(u)&&(u=u[0]),n.splice(0,o,u);break}s=n.join("/"),s+=t||(/^data\:|^blob\:|\?/.test(s)||i?"":".js"),s=("/"===s.charAt(0)||s.match(/^[\w\+\.\-]+:/)?"":y.baseUrl)+s}return y.urlArgs&&!/^blob\:/.test(s)?s+y.urlArgs(e,s):s},load:function(e,t){req.load(q,e,t)},execCb:function(e,t,i,r){return t.apply(r,i)},onScriptLoad:function(e){if("load"===e.type||readyRegExp.test((e.currentTarget||e.srcElement).readyState)){interactiveScript=null;var t=g(e);q.completeLoad(t.id)}},onScriptError:function(e){var t=g(e);if(!n(t.id)){var i=[];return eachProp(S,function(e,r){0!==r.indexOf("_@r")&&each(e.depMaps,function(e){if(e.id===t.id)return i.push(r),!0})}),c(makeError("scripterror",'Script error for "'+t.id+(i.length?'", needed by: '+i.join(", "):'"'),e,[t.id]))}}},q.require=q.makeRequire(),q}function getInteractiveScript(){return interactiveScript&&"interactive"===interactiveScript.readyState?interactiveScript:(eachReverse(scripts(),function(e){if("interactive"===e.readyState)return interactiveScript=e}),interactiveScript)}var req,s,head,baseElement,dataMain,src,interactiveScript,currentlyAddingScript,mainScript,subPath,version="2.3.3",commentRegExp=/\/\*[\s\S]*?\*\/|([^:"'=]|^)\/\/.*$/gm,cjsRequireRegExp=/[^.]\s*require\s*\(\s*["']([^'"\s]+)["']\s*\)/g,jsSuffixRegExp=/\.js$/,currDirRegExp=/^\.\//,op=Object.prototype,ostring=op.toString,hasOwn=op.hasOwnProperty,isBrowser=!("undefined"==typeof window||"undefined"==typeof navigator||!window.document),isWebWorker=!isBrowser&&"undefined"!=typeof importScripts,readyRegExp=isBrowser&&"PLAYSTATION 3"===navigator.platform?/^complete$/:/^(complete|loaded)$/,defContextName="_",isOpera="undefined"!=typeof opera&&"[object Opera]"===opera.toString(),contexts={},cfg={},globalDefQueue=[],useInteractive=!1;if("undefined"==typeof define){if("undefined"!=typeof requirejs){if(isFunction(requirejs))return;cfg=requirejs,requirejs=void 0}"undefined"==typeof require||isFunction(require)||(cfg=require,require=void 0),req=requirejs=function(e,t,i,r){var n,o,a=defContextName;return isArray(e)||"string"==typeof e||(o=e,isArray(t)?(e=t,t=i,i=r):e=[]),o&&o.context&&(a=o.context),n=getOwn(contexts,a),n||(n=contexts[a]=req.s.newContext(a)),o&&n.configure(o),n.require(e,t,i)},req.config=function(e){return req(e)},req.nextTick="undefined"!=typeof setTimeout?function(e){setTimeout(e,4)}:function(e){e()},require||(require=req),req.version=version,req.jsExtRegExp=/^\/|:|\?|\.js$/,req.isBrowser=isBrowser,s=req.s={contexts:contexts,newContext:newContext},req({}),each(["toUrl","undef","defined","specified"],function(e){req[e]=function(){var t=contexts[defContextName];return t.require[e].apply(t,arguments)}}),isBrowser&&(head=s.head=document.getElementsByTagName("head")[0],baseElement=document.getElementsByTagName("base")[0],baseElement&&(head=s.head=baseElement.parentNode)),req.onError=defaultOnError,req.createNode=function(e,t,i){var r=e.xhtml?document.createElementNS("http://www.w3.org/1999/xhtml","html:script"):document.createElement("script");return r.type=e.scriptType||"text/javascript",r.charset="utf-8",r.async=!0,r},req.load=function(e,t,i){var r,n=e&&e.config||{};if(isBrowser)return r=req.createNode(n,t,i),r.setAttribute("data-requirecontext",e.contextName),r.setAttribute("data-requiremodule",t),!r.attachEvent||r.attachEvent.toString&&r.attachEvent.toString().indexOf("[native code")<0||isOpera?(r.addEventListener("load",e.onScriptLoad,!1),r.addEventListener("error",e.onScriptError,!1)):(useInteractive=!0,r.attachEvent("onreadystatechange",e.onScriptLoad)),r.src=i,n.onNodeCreated&&n.onNodeCreated(r,n,t,i),currentlyAddingScript=r,baseElement?head.insertBefore(r,baseElement):head.appendChild(r),currentlyAddingScript=null,r;if(isWebWorker)try{setTimeout(function(){},0),importScripts(i),e.completeLoad(t)}catch(r){e.onError(makeError("importscripts","importScripts failed for "+t+" at "+i,r,[t]))}},isBrowser&&!cfg.skipDataMain&&eachReverse(scripts(),function(e){if(head||(head=e.parentNode),dataMain=e.getAttribute("data-main"))return mainScript=dataMain,cfg.baseUrl||mainScript.indexOf("!")!==-1||(src=mainScript.split("/"),mainScript=src.pop(),subPath=src.length?src.join("/")+"/":"./",cfg.baseUrl=subPath),mainScript=mainScript.replace(jsSuffixRegExp,""),req.jsExtRegExp.test(mainScript)&&(mainScript=dataMain),cfg.deps=cfg.deps?cfg.deps.concat(mainScript):[mainScript],!0}),define=function(e,t,i){var r,n;"string"!=typeof e&&(i=t,t=e,e=null),isArray(t)||(i=t,t=null),!t&&isFunction(i)&&(t=[],i.length&&(i.toString().replace(commentRegExp,commentReplace).replace(cjsRequireRegExp,function(e,i){t.push(i)}),t=(1===i.length?["require"]:["require","exports","module"]).concat(t))),useInteractive&&(r=currentlyAddingScript||getInteractiveScript(),r&&(e||(e=r.getAttribute("data-requiremodule")),n=contexts[r.getAttribute("data-requirecontext")])),n?(n.defQueue.push([e,t,i]),n.defQueueMap[e]=!0):globalDefQueue.push([e,t,i])},define.amd={jQuery:!0},req.exec=function(text){return eval(text)},req(cfg)}}(this,"undefined"==typeof setTimeout?void 0:setTimeout);


// --- jQuery-lib ---
/*! jQuery v3.2.1 | (c) JS Foundation and other contributors | jquery.org/license */
!function(a,b){"use strict";"object"==typeof module&&"object"==typeof module.exports?module.exports=a.document?b(a,!0):function(a){if(!a.document)throw new Error("jQuery requires a window with a document");return b(a)}:b(a)}("undefined"!=typeof window?window:this,function(a,b){"use strict";var c=[],d=a.document,e=Object.getPrototypeOf,f=c.slice,g=c.concat,h=c.push,i=c.indexOf,j={},k=j.toString,l=j.hasOwnProperty,m=l.toString,n=m.call(Object),o={};function p(a,b){b=b||d;var c=b.createElement("script");c.text=a,b.head.appendChild(c).parentNode.removeChild(c)}var q="3.2.1",r=function(a,b){return new r.fn.init(a,b)},s=/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,t=/^-ms-/,u=/-([a-z])/g,v=function(a,b){return b.toUpperCase()};r.fn=r.prototype={jquery:q,constructor:r,length:0,toArray:function(){return f.call(this)},get:function(a){return null==a?f.call(this):a<0?this[a+this.length]:this[a]},pushStack:function(a){var b=r.merge(this.constructor(),a);return b.prevObject=this,b},each:function(a){return r.each(this,a)},map:function(a){return this.pushStack(r.map(this,function(b,c){return a.call(b,c,b)}))},slice:function(){return this.pushStack(f.apply(this,arguments))},first:function(){return this.eq(0)},last:function(){return this.eq(-1)},eq:function(a){var b=this.length,c=+a+(a<0?b:0);return this.pushStack(c>=0&&c<b?[this[c]]:[])},end:function(){return this.prevObject||this.constructor()},push:h,sort:c.sort,splice:c.splice},r.extend=r.fn.extend=function(){var a,b,c,d,e,f,g=arguments[0]||{},h=1,i=arguments.length,j=!1;for("boolean"==typeof g&&(j=g,g=arguments[h]||{},h++),"object"==typeof g||r.isFunction(g)||(g={}),h===i&&(g=this,h--);h<i;h++)if(null!=(a=arguments[h]))for(b in a)c=g[b],d=a[b],g!==d&&(j&&d&&(r.isPlainObject(d)||(e=Array.isArray(d)))?(e?(e=!1,f=c&&Array.isArray(c)?c:[]):f=c&&r.isPlainObject(c)?c:{},g[b]=r.extend(j,f,d)):void 0!==d&&(g[b]=d));return g},r.extend({expando:"jQuery"+(q+Math.random()).replace(/\D/g,""),isReady:!0,error:function(a){throw new Error(a)},noop:function(){},isFunction:function(a){return"function"===r.type(a)},isWindow:function(a){return null!=a&&a===a.window},isNumeric:function(a){var b=r.type(a);return("number"===b||"string"===b)&&!isNaN(a-parseFloat(a))},isPlainObject:function(a){var b,c;return!(!a||"[object Object]"!==k.call(a))&&(!(b=e(a))||(c=l.call(b,"constructor")&&b.constructor,"function"==typeof c&&m.call(c)===n))},isEmptyObject:function(a){var b;for(b in a)return!1;return!0},type:function(a){return null==a?a+"":"object"==typeof a||"function"==typeof a?j[k.call(a)]||"object":typeof a},globalEval:function(a){p(a)},camelCase:function(a){return a.replace(t,"ms-").replace(u,v)},each:function(a,b){var c,d=0;if(w(a)){for(c=a.length;d<c;d++)if(b.call(a[d],d,a[d])===!1)break}else for(d in a)if(b.call(a[d],d,a[d])===!1)break;return a},trim:function(a){return null==a?"":(a+"").replace(s,"")},makeArray:function(a,b){var c=b||[];return null!=a&&(w(Object(a))?r.merge(c,"string"==typeof a?[a]:a):h.call(c,a)),c},inArray:function(a,b,c){return null==b?-1:i.call(b,a,c)},merge:function(a,b){for(var c=+b.length,d=0,e=a.length;d<c;d++)a[e++]=b[d];return a.length=e,a},grep:function(a,b,c){for(var d,e=[],f=0,g=a.length,h=!c;f<g;f++)d=!b(a[f],f),d!==h&&e.push(a[f]);return e},map:function(a,b,c){var d,e,f=0,h=[];if(w(a))for(d=a.length;f<d;f++)e=b(a[f],f,c),null!=e&&h.push(e);else for(f in a)e=b(a[f],f,c),null!=e&&h.push(e);return g.apply([],h)},guid:1,proxy:function(a,b){var c,d,e;if("string"==typeof b&&(c=a[b],b=a,a=c),r.isFunction(a))return d=f.call(arguments,2),e=function(){return a.apply(b||this,d.concat(f.call(arguments)))},e.guid=a.guid=a.guid||r.guid++,e},now:Date.now,support:o}),"function"==typeof Symbol&&(r.fn[Symbol.iterator]=c[Symbol.iterator]),r.each("Boolean Number String Function Array Date RegExp Object Error Symbol".split(" "),function(a,b){j["[object "+b+"]"]=b.toLowerCase()});function w(a){var b=!!a&&"length"in a&&a.length,c=r.type(a);return"function"!==c&&!r.isWindow(a)&&("array"===c||0===b||"number"==typeof b&&b>0&&b-1 in a)}var x=function(a){var b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u="sizzle"+1*new Date,v=a.document,w=0,x=0,y=ha(),z=ha(),A=ha(),B=function(a,b){return a===b&&(l=!0),0},C={}.hasOwnProperty,D=[],E=D.pop,F=D.push,G=D.push,H=D.slice,I=function(a,b){for(var c=0,d=a.length;c<d;c++)if(a[c]===b)return c;return-1},J="checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",K="[\\x20\\t\\r\\n\\f]",L="(?:\\\\.|[\\w-]|[^\0-\\xa0])+",M="\\["+K+"*("+L+")(?:"+K+"*([*^$|!~]?=)"+K+"*(?:'((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\"|("+L+"))|)"+K+"*\\]",N=":("+L+")(?:\\((('((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\")|((?:\\\\.|[^\\\\()[\\]]|"+M+")*)|.*)\\)|)",O=new RegExp(K+"+","g"),P=new RegExp("^"+K+"+|((?:^|[^\\\\])(?:\\\\.)*)"+K+"+$","g"),Q=new RegExp("^"+K+"*,"+K+"*"),R=new RegExp("^"+K+"*([>+~]|"+K+")"+K+"*"),S=new RegExp("="+K+"*([^\\]'\"]*?)"+K+"*\\]","g"),T=new RegExp(N),U=new RegExp("^"+L+"$"),V={ID:new RegExp("^#("+L+")"),CLASS:new RegExp("^\\.("+L+")"),TAG:new RegExp("^("+L+"|[*])"),ATTR:new RegExp("^"+M),PSEUDO:new RegExp("^"+N),CHILD:new RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\("+K+"*(even|odd|(([+-]|)(\\d*)n|)"+K+"*(?:([+-]|)"+K+"*(\\d+)|))"+K+"*\\)|)","i"),bool:new RegExp("^(?:"+J+")$","i"),needsContext:new RegExp("^"+K+"*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\("+K+"*((?:-\\d)?\\d*)"+K+"*\\)|)(?=[^-]|$)","i")},W=/^(?:input|select|textarea|button)$/i,X=/^h\d$/i,Y=/^[^{]+\{\s*\[native \w/,Z=/^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,$=/[+~]/,_=new RegExp("\\\\([\\da-f]{1,6}"+K+"?|("+K+")|.)","ig"),aa=function(a,b,c){var d="0x"+b-65536;return d!==d||c?b:d<0?String.fromCharCode(d+65536):String.fromCharCode(d>>10|55296,1023&d|56320)},ba=/([\0-\x1f\x7f]|^-?\d)|^-$|[^\0-\x1f\x7f-\uFFFF\w-]/g,ca=function(a,b){return b?"\0"===a?"\ufffd":a.slice(0,-1)+"\\"+a.charCodeAt(a.length-1).toString(16)+" ":"\\"+a},da=function(){m()},ea=ta(function(a){return a.disabled===!0&&("form"in a||"label"in a)},{dir:"parentNode",next:"legend"});try{G.apply(D=H.call(v.childNodes),v.childNodes),D[v.childNodes.length].nodeType}catch(fa){G={apply:D.length?function(a,b){F.apply(a,H.call(b))}:function(a,b){var c=a.length,d=0;while(a[c++]=b[d++]);a.length=c-1}}}function ga(a,b,d,e){var f,h,j,k,l,o,r,s=b&&b.ownerDocument,w=b?b.nodeType:9;if(d=d||[],"string"!=typeof a||!a||1!==w&&9!==w&&11!==w)return d;if(!e&&((b?b.ownerDocument||b:v)!==n&&m(b),b=b||n,p)){if(11!==w&&(l=Z.exec(a)))if(f=l[1]){if(9===w){if(!(j=b.getElementById(f)))return d;if(j.id===f)return d.push(j),d}else if(s&&(j=s.getElementById(f))&&t(b,j)&&j.id===f)return d.push(j),d}else{if(l[2])return G.apply(d,b.getElementsByTagName(a)),d;if((f=l[3])&&c.getElementsByClassName&&b.getElementsByClassName)return G.apply(d,b.getElementsByClassName(f)),d}if(c.qsa&&!A[a+" "]&&(!q||!q.test(a))){if(1!==w)s=b,r=a;else if("object"!==b.nodeName.toLowerCase()){(k=b.getAttribute("id"))?k=k.replace(ba,ca):b.setAttribute("id",k=u),o=g(a),h=o.length;while(h--)o[h]="#"+k+" "+sa(o[h]);r=o.join(","),s=$.test(a)&&qa(b.parentNode)||b}if(r)try{return G.apply(d,s.querySelectorAll(r)),d}catch(x){}finally{k===u&&b.removeAttribute("id")}}}return i(a.replace(P,"$1"),b,d,e)}function ha(){var a=[];function b(c,e){return a.push(c+" ")>d.cacheLength&&delete b[a.shift()],b[c+" "]=e}return b}function ia(a){return a[u]=!0,a}function ja(a){var b=n.createElement("fieldset");try{return!!a(b)}catch(c){return!1}finally{b.parentNode&&b.parentNode.removeChild(b),b=null}}function ka(a,b){var c=a.split("|"),e=c.length;while(e--)d.attrHandle[c[e]]=b}function la(a,b){var c=b&&a,d=c&&1===a.nodeType&&1===b.nodeType&&a.sourceIndex-b.sourceIndex;if(d)return d;if(c)while(c=c.nextSibling)if(c===b)return-1;return a?1:-1}function ma(a){return function(b){var c=b.nodeName.toLowerCase();return"input"===c&&b.type===a}}function na(a){return function(b){var c=b.nodeName.toLowerCase();return("input"===c||"button"===c)&&b.type===a}}function oa(a){return function(b){return"form"in b?b.parentNode&&b.disabled===!1?"label"in b?"label"in b.parentNode?b.parentNode.disabled===a:b.disabled===a:b.isDisabled===a||b.isDisabled!==!a&&ea(b)===a:b.disabled===a:"label"in b&&b.disabled===a}}function pa(a){return ia(function(b){return b=+b,ia(function(c,d){var e,f=a([],c.length,b),g=f.length;while(g--)c[e=f[g]]&&(c[e]=!(d[e]=c[e]))})})}function qa(a){return a&&"undefined"!=typeof a.getElementsByTagName&&a}c=ga.support={},f=ga.isXML=function(a){var b=a&&(a.ownerDocument||a).documentElement;return!!b&&"HTML"!==b.nodeName},m=ga.setDocument=function(a){var b,e,g=a?a.ownerDocument||a:v;return g!==n&&9===g.nodeType&&g.documentElement?(n=g,o=n.documentElement,p=!f(n),v!==n&&(e=n.defaultView)&&e.top!==e&&(e.addEventListener?e.addEventListener("unload",da,!1):e.attachEvent&&e.attachEvent("onunload",da)),c.attributes=ja(function(a){return a.className="i",!a.getAttribute("className")}),c.getElementsByTagName=ja(function(a){return a.appendChild(n.createComment("")),!a.getElementsByTagName("*").length}),c.getElementsByClassName=Y.test(n.getElementsByClassName),c.getById=ja(function(a){return o.appendChild(a).id=u,!n.getElementsByName||!n.getElementsByName(u).length}),c.getById?(d.filter.ID=function(a){var b=a.replace(_,aa);return function(a){return a.getAttribute("id")===b}},d.find.ID=function(a,b){if("undefined"!=typeof b.getElementById&&p){var c=b.getElementById(a);return c?[c]:[]}}):(d.filter.ID=function(a){var b=a.replace(_,aa);return function(a){var c="undefined"!=typeof a.getAttributeNode&&a.getAttributeNode("id");return c&&c.value===b}},d.find.ID=function(a,b){if("undefined"!=typeof b.getElementById&&p){var c,d,e,f=b.getElementById(a);if(f){if(c=f.getAttributeNode("id"),c&&c.value===a)return[f];e=b.getElementsByName(a),d=0;while(f=e[d++])if(c=f.getAttributeNode("id"),c&&c.value===a)return[f]}return[]}}),d.find.TAG=c.getElementsByTagName?function(a,b){return"undefined"!=typeof b.getElementsByTagName?b.getElementsByTagName(a):c.qsa?b.querySelectorAll(a):void 0}:function(a,b){var c,d=[],e=0,f=b.getElementsByTagName(a);if("*"===a){while(c=f[e++])1===c.nodeType&&d.push(c);return d}return f},d.find.CLASS=c.getElementsByClassName&&function(a,b){if("undefined"!=typeof b.getElementsByClassName&&p)return b.getElementsByClassName(a)},r=[],q=[],(c.qsa=Y.test(n.querySelectorAll))&&(ja(function(a){o.appendChild(a).innerHTML="<a id='"+u+"'></a><select id='"+u+"-\r\\' msallowcapture=''><option selected=''></option></select>",a.querySelectorAll("[msallowcapture^='']").length&&q.push("[*^$]="+K+"*(?:''|\"\")"),a.querySelectorAll("[selected]").length||q.push("\\["+K+"*(?:value|"+J+")"),a.querySelectorAll("[id~="+u+"-]").length||q.push("~="),a.querySelectorAll(":checked").length||q.push(":checked"),a.querySelectorAll("a#"+u+"+*").length||q.push(".#.+[+~]")}),ja(function(a){a.innerHTML="<a href='' disabled='disabled'></a><select disabled='disabled'><option/></select>";var b=n.createElement("input");b.setAttribute("type","hidden"),a.appendChild(b).setAttribute("name","D"),a.querySelectorAll("[name=d]").length&&q.push("name"+K+"*[*^$|!~]?="),2!==a.querySelectorAll(":enabled").length&&q.push(":enabled",":disabled"),o.appendChild(a).disabled=!0,2!==a.querySelectorAll(":disabled").length&&q.push(":enabled",":disabled"),a.querySelectorAll("*,:x"),q.push(",.*:")})),(c.matchesSelector=Y.test(s=o.matches||o.webkitMatchesSelector||o.mozMatchesSelector||o.oMatchesSelector||o.msMatchesSelector))&&ja(function(a){c.disconnectedMatch=s.call(a,"*"),s.call(a,"[s!='']:x"),r.push("!=",N)}),q=q.length&&new RegExp(q.join("|")),r=r.length&&new RegExp(r.join("|")),b=Y.test(o.compareDocumentPosition),t=b||Y.test(o.contains)?function(a,b){var c=9===a.nodeType?a.documentElement:a,d=b&&b.parentNode;return a===d||!(!d||1!==d.nodeType||!(c.contains?c.contains(d):a.compareDocumentPosition&&16&a.compareDocumentPosition(d)))}:function(a,b){if(b)while(b=b.parentNode)if(b===a)return!0;return!1},B=b?function(a,b){if(a===b)return l=!0,0;var d=!a.compareDocumentPosition-!b.compareDocumentPosition;return d?d:(d=(a.ownerDocument||a)===(b.ownerDocument||b)?a.compareDocumentPosition(b):1,1&d||!c.sortDetached&&b.compareDocumentPosition(a)===d?a===n||a.ownerDocument===v&&t(v,a)?-1:b===n||b.ownerDocument===v&&t(v,b)?1:k?I(k,a)-I(k,b):0:4&d?-1:1)}:function(a,b){if(a===b)return l=!0,0;var c,d=0,e=a.parentNode,f=b.parentNode,g=[a],h=[b];if(!e||!f)return a===n?-1:b===n?1:e?-1:f?1:k?I(k,a)-I(k,b):0;if(e===f)return la(a,b);c=a;while(c=c.parentNode)g.unshift(c);c=b;while(c=c.parentNode)h.unshift(c);while(g[d]===h[d])d++;return d?la(g[d],h[d]):g[d]===v?-1:h[d]===v?1:0},n):n},ga.matches=function(a,b){return ga(a,null,null,b)},ga.matchesSelector=function(a,b){if((a.ownerDocument||a)!==n&&m(a),b=b.replace(S,"='$1']"),c.matchesSelector&&p&&!A[b+" "]&&(!r||!r.test(b))&&(!q||!q.test(b)))try{var d=s.call(a,b);if(d||c.disconnectedMatch||a.document&&11!==a.document.nodeType)return d}catch(e){}return ga(b,n,null,[a]).length>0},ga.contains=function(a,b){return(a.ownerDocument||a)!==n&&m(a),t(a,b)},ga.attr=function(a,b){(a.ownerDocument||a)!==n&&m(a);var e=d.attrHandle[b.toLowerCase()],f=e&&C.call(d.attrHandle,b.toLowerCase())?e(a,b,!p):void 0;return void 0!==f?f:c.attributes||!p?a.getAttribute(b):(f=a.getAttributeNode(b))&&f.specified?f.value:null},ga.escape=function(a){return(a+"").replace(ba,ca)},ga.error=function(a){throw new Error("Syntax error, unrecognized expression: "+a)},ga.uniqueSort=function(a){var b,d=[],e=0,f=0;if(l=!c.detectDuplicates,k=!c.sortStable&&a.slice(0),a.sort(B),l){while(b=a[f++])b===a[f]&&(e=d.push(f));while(e--)a.splice(d[e],1)}return k=null,a},e=ga.getText=function(a){var b,c="",d=0,f=a.nodeType;if(f){if(1===f||9===f||11===f){if("string"==typeof a.textContent)return a.textContent;for(a=a.firstChild;a;a=a.nextSibling)c+=e(a)}else if(3===f||4===f)return a.nodeValue}else while(b=a[d++])c+=e(b);return c},d=ga.selectors={cacheLength:50,createPseudo:ia,match:V,attrHandle:{},find:{},relative:{">":{dir:"parentNode",first:!0}," ":{dir:"parentNode"},"+":{dir:"previousSibling",first:!0},"~":{dir:"previousSibling"}},preFilter:{ATTR:function(a){return a[1]=a[1].replace(_,aa),a[3]=(a[3]||a[4]||a[5]||"").replace(_,aa),"~="===a[2]&&(a[3]=" "+a[3]+" "),a.slice(0,4)},CHILD:function(a){return a[1]=a[1].toLowerCase(),"nth"===a[1].slice(0,3)?(a[3]||ga.error(a[0]),a[4]=+(a[4]?a[5]+(a[6]||1):2*("even"===a[3]||"odd"===a[3])),a[5]=+(a[7]+a[8]||"odd"===a[3])):a[3]&&ga.error(a[0]),a},PSEUDO:function(a){var b,c=!a[6]&&a[2];return V.CHILD.test(a[0])?null:(a[3]?a[2]=a[4]||a[5]||"":c&&T.test(c)&&(b=g(c,!0))&&(b=c.indexOf(")",c.length-b)-c.length)&&(a[0]=a[0].slice(0,b),a[2]=c.slice(0,b)),a.slice(0,3))}},filter:{TAG:function(a){var b=a.replace(_,aa).toLowerCase();return"*"===a?function(){return!0}:function(a){return a.nodeName&&a.nodeName.toLowerCase()===b}},CLASS:function(a){var b=y[a+" "];return b||(b=new RegExp("(^|"+K+")"+a+"("+K+"|$)"))&&y(a,function(a){return b.test("string"==typeof a.className&&a.className||"undefined"!=typeof a.getAttribute&&a.getAttribute("class")||"")})},ATTR:function(a,b,c){return function(d){var e=ga.attr(d,a);return null==e?"!="===b:!b||(e+="","="===b?e===c:"!="===b?e!==c:"^="===b?c&&0===e.indexOf(c):"*="===b?c&&e.indexOf(c)>-1:"$="===b?c&&e.slice(-c.length)===c:"~="===b?(" "+e.replace(O," ")+" ").indexOf(c)>-1:"|="===b&&(e===c||e.slice(0,c.length+1)===c+"-"))}},CHILD:function(a,b,c,d,e){var f="nth"!==a.slice(0,3),g="last"!==a.slice(-4),h="of-type"===b;return 1===d&&0===e?function(a){return!!a.parentNode}:function(b,c,i){var j,k,l,m,n,o,p=f!==g?"nextSibling":"previousSibling",q=b.parentNode,r=h&&b.nodeName.toLowerCase(),s=!i&&!h,t=!1;if(q){if(f){while(p){m=b;while(m=m[p])if(h?m.nodeName.toLowerCase()===r:1===m.nodeType)return!1;o=p="only"===a&&!o&&"nextSibling"}return!0}if(o=[g?q.firstChild:q.lastChild],g&&s){m=q,l=m[u]||(m[u]={}),k=l[m.uniqueID]||(l[m.uniqueID]={}),j=k[a]||[],n=j[0]===w&&j[1],t=n&&j[2],m=n&&q.childNodes[n];while(m=++n&&m&&m[p]||(t=n=0)||o.pop())if(1===m.nodeType&&++t&&m===b){k[a]=[w,n,t];break}}else if(s&&(m=b,l=m[u]||(m[u]={}),k=l[m.uniqueID]||(l[m.uniqueID]={}),j=k[a]||[],n=j[0]===w&&j[1],t=n),t===!1)while(m=++n&&m&&m[p]||(t=n=0)||o.pop())if((h?m.nodeName.toLowerCase()===r:1===m.nodeType)&&++t&&(s&&(l=m[u]||(m[u]={}),k=l[m.uniqueID]||(l[m.uniqueID]={}),k[a]=[w,t]),m===b))break;return t-=e,t===d||t%d===0&&t/d>=0}}},PSEUDO:function(a,b){var c,e=d.pseudos[a]||d.setFilters[a.toLowerCase()]||ga.error("unsupported pseudo: "+a);return e[u]?e(b):e.length>1?(c=[a,a,"",b],d.setFilters.hasOwnProperty(a.toLowerCase())?ia(function(a,c){var d,f=e(a,b),g=f.length;while(g--)d=I(a,f[g]),a[d]=!(c[d]=f[g])}):function(a){return e(a,0,c)}):e}},pseudos:{not:ia(function(a){var b=[],c=[],d=h(a.replace(P,"$1"));return d[u]?ia(function(a,b,c,e){var f,g=d(a,null,e,[]),h=a.length;while(h--)(f=g[h])&&(a[h]=!(b[h]=f))}):function(a,e,f){return b[0]=a,d(b,null,f,c),b[0]=null,!c.pop()}}),has:ia(function(a){return function(b){return ga(a,b).length>0}}),contains:ia(function(a){return a=a.replace(_,aa),function(b){return(b.textContent||b.innerText||e(b)).indexOf(a)>-1}}),lang:ia(function(a){return U.test(a||"")||ga.error("unsupported lang: "+a),a=a.replace(_,aa).toLowerCase(),function(b){var c;do if(c=p?b.lang:b.getAttribute("xml:lang")||b.getAttribute("lang"))return c=c.toLowerCase(),c===a||0===c.indexOf(a+"-");while((b=b.parentNode)&&1===b.nodeType);return!1}}),target:function(b){var c=a.location&&a.location.hash;return c&&c.slice(1)===b.id},root:function(a){return a===o},focus:function(a){return a===n.activeElement&&(!n.hasFocus||n.hasFocus())&&!!(a.type||a.href||~a.tabIndex)},enabled:oa(!1),disabled:oa(!0),checked:function(a){var b=a.nodeName.toLowerCase();return"input"===b&&!!a.checked||"option"===b&&!!a.selected},selected:function(a){return a.parentNode&&a.parentNode.selectedIndex,a.selected===!0},empty:function(a){for(a=a.firstChild;a;a=a.nextSibling)if(a.nodeType<6)return!1;return!0},parent:function(a){return!d.pseudos.empty(a)},header:function(a){return X.test(a.nodeName)},input:function(a){return W.test(a.nodeName)},button:function(a){var b=a.nodeName.toLowerCase();return"input"===b&&"button"===a.type||"button"===b},text:function(a){var b;return"input"===a.nodeName.toLowerCase()&&"text"===a.type&&(null==(b=a.getAttribute("type"))||"text"===b.toLowerCase())},first:pa(function(){return[0]}),last:pa(function(a,b){return[b-1]}),eq:pa(function(a,b,c){return[c<0?c+b:c]}),even:pa(function(a,b){for(var c=0;c<b;c+=2)a.push(c);return a}),odd:pa(function(a,b){for(var c=1;c<b;c+=2)a.push(c);return a}),lt:pa(function(a,b,c){for(var d=c<0?c+b:c;--d>=0;)a.push(d);return a}),gt:pa(function(a,b,c){for(var d=c<0?c+b:c;++d<b;)a.push(d);return a})}},d.pseudos.nth=d.pseudos.eq;for(b in{radio:!0,checkbox:!0,file:!0,password:!0,image:!0})d.pseudos[b]=ma(b);for(b in{submit:!0,reset:!0})d.pseudos[b]=na(b);function ra(){}ra.prototype=d.filters=d.pseudos,d.setFilters=new ra,g=ga.tokenize=function(a,b){var c,e,f,g,h,i,j,k=z[a+" "];if(k)return b?0:k.slice(0);h=a,i=[],j=d.preFilter;while(h){c&&!(e=Q.exec(h))||(e&&(h=h.slice(e[0].length)||h),i.push(f=[])),c=!1,(e=R.exec(h))&&(c=e.shift(),f.push({value:c,type:e[0].replace(P," ")}),h=h.slice(c.length));for(g in d.filter)!(e=V[g].exec(h))||j[g]&&!(e=j[g](e))||(c=e.shift(),f.push({value:c,type:g,matches:e}),h=h.slice(c.length));if(!c)break}return b?h.length:h?ga.error(a):z(a,i).slice(0)};function sa(a){for(var b=0,c=a.length,d="";b<c;b++)d+=a[b].value;return d}function ta(a,b,c){var d=b.dir,e=b.next,f=e||d,g=c&&"parentNode"===f,h=x++;return b.first?function(b,c,e){while(b=b[d])if(1===b.nodeType||g)return a(b,c,e);return!1}:function(b,c,i){var j,k,l,m=[w,h];if(i){while(b=b[d])if((1===b.nodeType||g)&&a(b,c,i))return!0}else while(b=b[d])if(1===b.nodeType||g)if(l=b[u]||(b[u]={}),k=l[b.uniqueID]||(l[b.uniqueID]={}),e&&e===b.nodeName.toLowerCase())b=b[d]||b;else{if((j=k[f])&&j[0]===w&&j[1]===h)return m[2]=j[2];if(k[f]=m,m[2]=a(b,c,i))return!0}return!1}}function ua(a){return a.length>1?function(b,c,d){var e=a.length;while(e--)if(!a[e](b,c,d))return!1;return!0}:a[0]}function va(a,b,c){for(var d=0,e=b.length;d<e;d++)ga(a,b[d],c);return c}function wa(a,b,c,d,e){for(var f,g=[],h=0,i=a.length,j=null!=b;h<i;h++)(f=a[h])&&(c&&!c(f,d,e)||(g.push(f),j&&b.push(h)));return g}function xa(a,b,c,d,e,f){return d&&!d[u]&&(d=xa(d)),e&&!e[u]&&(e=xa(e,f)),ia(function(f,g,h,i){var j,k,l,m=[],n=[],o=g.length,p=f||va(b||"*",h.nodeType?[h]:h,[]),q=!a||!f&&b?p:wa(p,m,a,h,i),r=c?e||(f?a:o||d)?[]:g:q;if(c&&c(q,r,h,i),d){j=wa(r,n),d(j,[],h,i),k=j.length;while(k--)(l=j[k])&&(r[n[k]]=!(q[n[k]]=l))}if(f){if(e||a){if(e){j=[],k=r.length;while(k--)(l=r[k])&&j.push(q[k]=l);e(null,r=[],j,i)}k=r.length;while(k--)(l=r[k])&&(j=e?I(f,l):m[k])>-1&&(f[j]=!(g[j]=l))}}else r=wa(r===g?r.splice(o,r.length):r),e?e(null,g,r,i):G.apply(g,r)})}function ya(a){for(var b,c,e,f=a.length,g=d.relative[a[0].type],h=g||d.relative[" "],i=g?1:0,k=ta(function(a){return a===b},h,!0),l=ta(function(a){return I(b,a)>-1},h,!0),m=[function(a,c,d){var e=!g&&(d||c!==j)||((b=c).nodeType?k(a,c,d):l(a,c,d));return b=null,e}];i<f;i++)if(c=d.relative[a[i].type])m=[ta(ua(m),c)];else{if(c=d.filter[a[i].type].apply(null,a[i].matches),c[u]){for(e=++i;e<f;e++)if(d.relative[a[e].type])break;return xa(i>1&&ua(m),i>1&&sa(a.slice(0,i-1).concat({value:" "===a[i-2].type?"*":""})).replace(P,"$1"),c,i<e&&ya(a.slice(i,e)),e<f&&ya(a=a.slice(e)),e<f&&sa(a))}m.push(c)}return ua(m)}function za(a,b){var c=b.length>0,e=a.length>0,f=function(f,g,h,i,k){var l,o,q,r=0,s="0",t=f&&[],u=[],v=j,x=f||e&&d.find.TAG("*",k),y=w+=null==v?1:Math.random()||.1,z=x.length;for(k&&(j=g===n||g||k);s!==z&&null!=(l=x[s]);s++){if(e&&l){o=0,g||l.ownerDocument===n||(m(l),h=!p);while(q=a[o++])if(q(l,g||n,h)){i.push(l);break}k&&(w=y)}c&&((l=!q&&l)&&r--,f&&t.push(l))}if(r+=s,c&&s!==r){o=0;while(q=b[o++])q(t,u,g,h);if(f){if(r>0)while(s--)t[s]||u[s]||(u[s]=E.call(i));u=wa(u)}G.apply(i,u),k&&!f&&u.length>0&&r+b.length>1&&ga.uniqueSort(i)}return k&&(w=y,j=v),t};return c?ia(f):f}return h=ga.compile=function(a,b){var c,d=[],e=[],f=A[a+" "];if(!f){b||(b=g(a)),c=b.length;while(c--)f=ya(b[c]),f[u]?d.push(f):e.push(f);f=A(a,za(e,d)),f.selector=a}return f},i=ga.select=function(a,b,c,e){var f,i,j,k,l,m="function"==typeof a&&a,n=!e&&g(a=m.selector||a);if(c=c||[],1===n.length){if(i=n[0]=n[0].slice(0),i.length>2&&"ID"===(j=i[0]).type&&9===b.nodeType&&p&&d.relative[i[1].type]){if(b=(d.find.ID(j.matches[0].replace(_,aa),b)||[])[0],!b)return c;m&&(b=b.parentNode),a=a.slice(i.shift().value.length)}f=V.needsContext.test(a)?0:i.length;while(f--){if(j=i[f],d.relative[k=j.type])break;if((l=d.find[k])&&(e=l(j.matches[0].replace(_,aa),$.test(i[0].type)&&qa(b.parentNode)||b))){if(i.splice(f,1),a=e.length&&sa(i),!a)return G.apply(c,e),c;break}}}return(m||h(a,n))(e,b,!p,c,!b||$.test(a)&&qa(b.parentNode)||b),c},c.sortStable=u.split("").sort(B).join("")===u,c.detectDuplicates=!!l,m(),c.sortDetached=ja(function(a){return 1&a.compareDocumentPosition(n.createElement("fieldset"))}),ja(function(a){return a.innerHTML="<a href='#'></a>","#"===a.firstChild.getAttribute("href")})||ka("type|href|height|width",function(a,b,c){if(!c)return a.getAttribute(b,"type"===b.toLowerCase()?1:2)}),c.attributes&&ja(function(a){return a.innerHTML="<input/>",a.firstChild.setAttribute("value",""),""===a.firstChild.getAttribute("value")})||ka("value",function(a,b,c){if(!c&&"input"===a.nodeName.toLowerCase())return a.defaultValue}),ja(function(a){return null==a.getAttribute("disabled")})||ka(J,function(a,b,c){var d;if(!c)return a[b]===!0?b.toLowerCase():(d=a.getAttributeNode(b))&&d.specified?d.value:null}),ga}(a);r.find=x,r.expr=x.selectors,r.expr[":"]=r.expr.pseudos,r.uniqueSort=r.unique=x.uniqueSort,r.text=x.getText,r.isXMLDoc=x.isXML,r.contains=x.contains,r.escapeSelector=x.escape;var y=function(a,b,c){var d=[],e=void 0!==c;while((a=a[b])&&9!==a.nodeType)if(1===a.nodeType){if(e&&r(a).is(c))break;d.push(a)}return d},z=function(a,b){for(var c=[];a;a=a.nextSibling)1===a.nodeType&&a!==b&&c.push(a);return c},A=r.expr.match.needsContext;function B(a,b){return a.nodeName&&a.nodeName.toLowerCase()===b.toLowerCase()}var C=/^<([a-z][^\/\0>:\x20\t\r\n\f]*)[\x20\t\r\n\f]*\/?>(?:<\/\1>|)$/i,D=/^.[^:#\[\.,]*$/;function E(a,b,c){return r.isFunction(b)?r.grep(a,function(a,d){return!!b.call(a,d,a)!==c}):b.nodeType?r.grep(a,function(a){return a===b!==c}):"string"!=typeof b?r.grep(a,function(a){return i.call(b,a)>-1!==c}):D.test(b)?r.filter(b,a,c):(b=r.filter(b,a),r.grep(a,function(a){return i.call(b,a)>-1!==c&&1===a.nodeType}))}r.filter=function(a,b,c){var d=b[0];return c&&(a=":not("+a+")"),1===b.length&&1===d.nodeType?r.find.matchesSelector(d,a)?[d]:[]:r.find.matches(a,r.grep(b,function(a){return 1===a.nodeType}))},r.fn.extend({find:function(a){var b,c,d=this.length,e=this;if("string"!=typeof a)return this.pushStack(r(a).filter(function(){for(b=0;b<d;b++)if(r.contains(e[b],this))return!0}));for(c=this.pushStack([]),b=0;b<d;b++)r.find(a,e[b],c);return d>1?r.uniqueSort(c):c},filter:function(a){return this.pushStack(E(this,a||[],!1))},not:function(a){return this.pushStack(E(this,a||[],!0))},is:function(a){return!!E(this,"string"==typeof a&&A.test(a)?r(a):a||[],!1).length}});var F,G=/^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]+))$/,H=r.fn.init=function(a,b,c){var e,f;if(!a)return this;if(c=c||F,"string"==typeof a){if(e="<"===a[0]&&">"===a[a.length-1]&&a.length>=3?[null,a,null]:G.exec(a),!e||!e[1]&&b)return!b||b.jquery?(b||c).find(a):this.constructor(b).find(a);if(e[1]){if(b=b instanceof r?b[0]:b,r.merge(this,r.parseHTML(e[1],b&&b.nodeType?b.ownerDocument||b:d,!0)),C.test(e[1])&&r.isPlainObject(b))for(e in b)r.isFunction(this[e])?this[e](b[e]):this.attr(e,b[e]);return this}return f=d.getElementById(e[2]),f&&(this[0]=f,this.length=1),this}return a.nodeType?(this[0]=a,this.length=1,this):r.isFunction(a)?void 0!==c.ready?c.ready(a):a(r):r.makeArray(a,this)};H.prototype=r.fn,F=r(d);var I=/^(?:parents|prev(?:Until|All))/,J={children:!0,contents:!0,next:!0,prev:!0};r.fn.extend({has:function(a){var b=r(a,this),c=b.length;return this.filter(function(){for(var a=0;a<c;a++)if(r.contains(this,b[a]))return!0})},closest:function(a,b){var c,d=0,e=this.length,f=[],g="string"!=typeof a&&r(a);if(!A.test(a))for(;d<e;d++)for(c=this[d];c&&c!==b;c=c.parentNode)if(c.nodeType<11&&(g?g.index(c)>-1:1===c.nodeType&&r.find.matchesSelector(c,a))){f.push(c);break}return this.pushStack(f.length>1?r.uniqueSort(f):f)},index:function(a){return a?"string"==typeof a?i.call(r(a),this[0]):i.call(this,a.jquery?a[0]:a):this[0]&&this[0].parentNode?this.first().prevAll().length:-1},add:function(a,b){return this.pushStack(r.uniqueSort(r.merge(this.get(),r(a,b))))},addBack:function(a){return this.add(null==a?this.prevObject:this.prevObject.filter(a))}});function K(a,b){while((a=a[b])&&1!==a.nodeType);return a}r.each({parent:function(a){var b=a.parentNode;return b&&11!==b.nodeType?b:null},parents:function(a){return y(a,"parentNode")},parentsUntil:function(a,b,c){return y(a,"parentNode",c)},next:function(a){return K(a,"nextSibling")},prev:function(a){return K(a,"previousSibling")},nextAll:function(a){return y(a,"nextSibling")},prevAll:function(a){return y(a,"previousSibling")},nextUntil:function(a,b,c){return y(a,"nextSibling",c)},prevUntil:function(a,b,c){return y(a,"previousSibling",c)},siblings:function(a){return z((a.parentNode||{}).firstChild,a)},children:function(a){return z(a.firstChild)},contents:function(a){return B(a,"iframe")?a.contentDocument:(B(a,"template")&&(a=a.content||a),r.merge([],a.childNodes))}},function(a,b){r.fn[a]=function(c,d){var e=r.map(this,b,c);return"Until"!==a.slice(-5)&&(d=c),d&&"string"==typeof d&&(e=r.filter(d,e)),this.length>1&&(J[a]||r.uniqueSort(e),I.test(a)&&e.reverse()),this.pushStack(e)}});var L=/[^\x20\t\r\n\f]+/g;function M(a){var b={};return r.each(a.match(L)||[],function(a,c){b[c]=!0}),b}r.Callbacks=function(a){a="string"==typeof a?M(a):r.extend({},a);var b,c,d,e,f=[],g=[],h=-1,i=function(){for(e=e||a.once,d=b=!0;g.length;h=-1){c=g.shift();while(++h<f.length)f[h].apply(c[0],c[1])===!1&&a.stopOnFalse&&(h=f.length,c=!1)}a.memory||(c=!1),b=!1,e&&(f=c?[]:"")},j={add:function(){return f&&(c&&!b&&(h=f.length-1,g.push(c)),function d(b){r.each(b,function(b,c){r.isFunction(c)?a.unique&&j.has(c)||f.push(c):c&&c.length&&"string"!==r.type(c)&&d(c)})}(arguments),c&&!b&&i()),this},remove:function(){return r.each(arguments,function(a,b){var c;while((c=r.inArray(b,f,c))>-1)f.splice(c,1),c<=h&&h--}),this},has:function(a){return a?r.inArray(a,f)>-1:f.length>0},empty:function(){return f&&(f=[]),this},disable:function(){return e=g=[],f=c="",this},disabled:function(){return!f},lock:function(){return e=g=[],c||b||(f=c=""),this},locked:function(){return!!e},fireWith:function(a,c){return e||(c=c||[],c=[a,c.slice?c.slice():c],g.push(c),b||i()),this},fire:function(){return j.fireWith(this,arguments),this},fired:function(){return!!d}};return j};function N(a){return a}function O(a){throw a}function P(a,b,c,d){var e;try{a&&r.isFunction(e=a.promise)?e.call(a).done(b).fail(c):a&&r.isFunction(e=a.then)?e.call(a,b,c):b.apply(void 0,[a].slice(d))}catch(a){c.apply(void 0,[a])}}r.extend({Deferred:function(b){var c=[["notify","progress",r.Callbacks("memory"),r.Callbacks("memory"),2],["resolve","done",r.Callbacks("once memory"),r.Callbacks("once memory"),0,"resolved"],["reject","fail",r.Callbacks("once memory"),r.Callbacks("once memory"),1,"rejected"]],d="pending",e={state:function(){return d},always:function(){return f.done(arguments).fail(arguments),this},"catch":function(a){return e.then(null,a)},pipe:function(){var a=arguments;return r.Deferred(function(b){r.each(c,function(c,d){var e=r.isFunction(a[d[4]])&&a[d[4]];f[d[1]](function(){var a=e&&e.apply(this,arguments);a&&r.isFunction(a.promise)?a.promise().progress(b.notify).done(b.resolve).fail(b.reject):b[d[0]+"With"](this,e?[a]:arguments)})}),a=null}).promise()},then:function(b,d,e){var f=0;function g(b,c,d,e){return function(){var h=this,i=arguments,j=function(){var a,j;if(!(b<f)){if(a=d.apply(h,i),a===c.promise())throw new TypeError("Thenable self-resolution");j=a&&("object"==typeof a||"function"==typeof a)&&a.then,r.isFunction(j)?e?j.call(a,g(f,c,N,e),g(f,c,O,e)):(f++,j.call(a,g(f,c,N,e),g(f,c,O,e),g(f,c,N,c.notifyWith))):(d!==N&&(h=void 0,i=[a]),(e||c.resolveWith)(h,i))}},k=e?j:function(){try{j()}catch(a){r.Deferred.exceptionHook&&r.Deferred.exceptionHook(a,k.stackTrace),b+1>=f&&(d!==O&&(h=void 0,i=[a]),c.rejectWith(h,i))}};b?k():(r.Deferred.getStackHook&&(k.stackTrace=r.Deferred.getStackHook()),a.setTimeout(k))}}return r.Deferred(function(a){c[0][3].add(g(0,a,r.isFunction(e)?e:N,a.notifyWith)),c[1][3].add(g(0,a,r.isFunction(b)?b:N)),c[2][3].add(g(0,a,r.isFunction(d)?d:O))}).promise()},promise:function(a){return null!=a?r.extend(a,e):e}},f={};return r.each(c,function(a,b){var g=b[2],h=b[5];e[b[1]]=g.add,h&&g.add(function(){d=h},c[3-a][2].disable,c[0][2].lock),g.add(b[3].fire),f[b[0]]=function(){return f[b[0]+"With"](this===f?void 0:this,arguments),this},f[b[0]+"With"]=g.fireWith}),e.promise(f),b&&b.call(f,f),f},when:function(a){var b=arguments.length,c=b,d=Array(c),e=f.call(arguments),g=r.Deferred(),h=function(a){return function(c){d[a]=this,e[a]=arguments.length>1?f.call(arguments):c,--b||g.resolveWith(d,e)}};if(b<=1&&(P(a,g.done(h(c)).resolve,g.reject,!b),"pending"===g.state()||r.isFunction(e[c]&&e[c].then)))return g.then();while(c--)P(e[c],h(c),g.reject);return g.promise()}});var Q=/^(Eval|Internal|Range|Reference|Syntax|Type|URI)Error$/;r.Deferred.exceptionHook=function(b,c){a.console&&a.console.warn&&b&&Q.test(b.name)&&a.console.warn("jQuery.Deferred exception: "+b.message,b.stack,c)},r.readyException=function(b){a.setTimeout(function(){throw b})};var R=r.Deferred();r.fn.ready=function(a){return R.then(a)["catch"](function(a){r.readyException(a)}),this},r.extend({isReady:!1,readyWait:1,ready:function(a){(a===!0?--r.readyWait:r.isReady)||(r.isReady=!0,a!==!0&&--r.readyWait>0||R.resolveWith(d,[r]))}}),r.ready.then=R.then;function S(){d.removeEventListener("DOMContentLoaded",S),
    a.removeEventListener("load",S),r.ready()}"complete"===d.readyState||"loading"!==d.readyState&&!d.documentElement.doScroll?a.setTimeout(r.ready):(d.addEventListener("DOMContentLoaded",S),a.addEventListener("load",S));var T=function(a,b,c,d,e,f,g){var h=0,i=a.length,j=null==c;if("object"===r.type(c)){e=!0;for(h in c)T(a,b,h,c[h],!0,f,g)}else if(void 0!==d&&(e=!0,r.isFunction(d)||(g=!0),j&&(g?(b.call(a,d),b=null):(j=b,b=function(a,b,c){return j.call(r(a),c)})),b))for(;h<i;h++)b(a[h],c,g?d:d.call(a[h],h,b(a[h],c)));return e?a:j?b.call(a):i?b(a[0],c):f},U=function(a){return 1===a.nodeType||9===a.nodeType||!+a.nodeType};function V(){this.expando=r.expando+V.uid++}V.uid=1,V.prototype={cache:function(a){var b=a[this.expando];return b||(b={},U(a)&&(a.nodeType?a[this.expando]=b:Object.defineProperty(a,this.expando,{value:b,configurable:!0}))),b},set:function(a,b,c){var d,e=this.cache(a);if("string"==typeof b)e[r.camelCase(b)]=c;else for(d in b)e[r.camelCase(d)]=b[d];return e},get:function(a,b){return void 0===b?this.cache(a):a[this.expando]&&a[this.expando][r.camelCase(b)]},access:function(a,b,c){return void 0===b||b&&"string"==typeof b&&void 0===c?this.get(a,b):(this.set(a,b,c),void 0!==c?c:b)},remove:function(a,b){var c,d=a[this.expando];if(void 0!==d){if(void 0!==b){Array.isArray(b)?b=b.map(r.camelCase):(b=r.camelCase(b),b=b in d?[b]:b.match(L)||[]),c=b.length;while(c--)delete d[b[c]]}(void 0===b||r.isEmptyObject(d))&&(a.nodeType?a[this.expando]=void 0:delete a[this.expando])}},hasData:function(a){var b=a[this.expando];return void 0!==b&&!r.isEmptyObject(b)}};var W=new V,X=new V,Y=/^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,Z=/[A-Z]/g;function $(a){return"true"===a||"false"!==a&&("null"===a?null:a===+a+""?+a:Y.test(a)?JSON.parse(a):a)}function _(a,b,c){var d;if(void 0===c&&1===a.nodeType)if(d="data-"+b.replace(Z,"-$&").toLowerCase(),c=a.getAttribute(d),"string"==typeof c){try{c=$(c)}catch(e){}X.set(a,b,c)}else c=void 0;return c}r.extend({hasData:function(a){return X.hasData(a)||W.hasData(a)},data:function(a,b,c){return X.access(a,b,c)},removeData:function(a,b){X.remove(a,b)},_data:function(a,b,c){return W.access(a,b,c)},_removeData:function(a,b){W.remove(a,b)}}),r.fn.extend({data:function(a,b){var c,d,e,f=this[0],g=f&&f.attributes;if(void 0===a){if(this.length&&(e=X.get(f),1===f.nodeType&&!W.get(f,"hasDataAttrs"))){c=g.length;while(c--)g[c]&&(d=g[c].name,0===d.indexOf("data-")&&(d=r.camelCase(d.slice(5)),_(f,d,e[d])));W.set(f,"hasDataAttrs",!0)}return e}return"object"==typeof a?this.each(function(){X.set(this,a)}):T(this,function(b){var c;if(f&&void 0===b){if(c=X.get(f,a),void 0!==c)return c;if(c=_(f,a),void 0!==c)return c}else this.each(function(){X.set(this,a,b)})},null,b,arguments.length>1,null,!0)},removeData:function(a){return this.each(function(){X.remove(this,a)})}}),r.extend({queue:function(a,b,c){var d;if(a)return b=(b||"fx")+"queue",d=W.get(a,b),c&&(!d||Array.isArray(c)?d=W.access(a,b,r.makeArray(c)):d.push(c)),d||[]},dequeue:function(a,b){b=b||"fx";var c=r.queue(a,b),d=c.length,e=c.shift(),f=r._queueHooks(a,b),g=function(){r.dequeue(a,b)};"inprogress"===e&&(e=c.shift(),d--),e&&("fx"===b&&c.unshift("inprogress"),delete f.stop,e.call(a,g,f)),!d&&f&&f.empty.fire()},_queueHooks:function(a,b){var c=b+"queueHooks";return W.get(a,c)||W.access(a,c,{empty:r.Callbacks("once memory").add(function(){W.remove(a,[b+"queue",c])})})}}),r.fn.extend({queue:function(a,b){var c=2;return"string"!=typeof a&&(b=a,a="fx",c--),arguments.length<c?r.queue(this[0],a):void 0===b?this:this.each(function(){var c=r.queue(this,a,b);r._queueHooks(this,a),"fx"===a&&"inprogress"!==c[0]&&r.dequeue(this,a)})},dequeue:function(a){return this.each(function(){r.dequeue(this,a)})},clearQueue:function(a){return this.queue(a||"fx",[])},promise:function(a,b){var c,d=1,e=r.Deferred(),f=this,g=this.length,h=function(){--d||e.resolveWith(f,[f])};"string"!=typeof a&&(b=a,a=void 0),a=a||"fx";while(g--)c=W.get(f[g],a+"queueHooks"),c&&c.empty&&(d++,c.empty.add(h));return h(),e.promise(b)}});var aa=/[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,ba=new RegExp("^(?:([+-])=|)("+aa+")([a-z%]*)$","i"),ca=["Top","Right","Bottom","Left"],da=function(a,b){return a=b||a,"none"===a.style.display||""===a.style.display&&r.contains(a.ownerDocument,a)&&"none"===r.css(a,"display")},ea=function(a,b,c,d){var e,f,g={};for(f in b)g[f]=a.style[f],a.style[f]=b[f];e=c.apply(a,d||[]);for(f in b)a.style[f]=g[f];return e};function fa(a,b,c,d){var e,f=1,g=20,h=d?function(){return d.cur()}:function(){return r.css(a,b,"")},i=h(),j=c&&c[3]||(r.cssNumber[b]?"":"px"),k=(r.cssNumber[b]||"px"!==j&&+i)&&ba.exec(r.css(a,b));if(k&&k[3]!==j){j=j||k[3],c=c||[],k=+i||1;do f=f||".5",k/=f,r.style(a,b,k+j);while(f!==(f=h()/i)&&1!==f&&--g)}return c&&(k=+k||+i||0,e=c[1]?k+(c[1]+1)*c[2]:+c[2],d&&(d.unit=j,d.start=k,d.end=e)),e}var ga={};function ha(a){var b,c=a.ownerDocument,d=a.nodeName,e=ga[d];return e?e:(b=c.body.appendChild(c.createElement(d)),e=r.css(b,"display"),b.parentNode.removeChild(b),"none"===e&&(e="block"),ga[d]=e,e)}function ia(a,b){for(var c,d,e=[],f=0,g=a.length;f<g;f++)d=a[f],d.style&&(c=d.style.display,b?("none"===c&&(e[f]=W.get(d,"display")||null,e[f]||(d.style.display="")),""===d.style.display&&da(d)&&(e[f]=ha(d))):"none"!==c&&(e[f]="none",W.set(d,"display",c)));for(f=0;f<g;f++)null!=e[f]&&(a[f].style.display=e[f]);return a}r.fn.extend({show:function(){return ia(this,!0)},hide:function(){return ia(this)},toggle:function(a){return"boolean"==typeof a?a?this.show():this.hide():this.each(function(){da(this)?r(this).show():r(this).hide()})}});var ja=/^(?:checkbox|radio)$/i,ka=/<([a-z][^\/\0>\x20\t\r\n\f]+)/i,la=/^$|\/(?:java|ecma)script/i,ma={option:[1,"<select multiple='multiple'>","</select>"],thead:[1,"<table>","</table>"],col:[2,"<table><colgroup>","</colgroup></table>"],tr:[2,"<table><tbody>","</tbody></table>"],td:[3,"<table><tbody><tr>","</tr></tbody></table>"],_default:[0,"",""]};ma.optgroup=ma.option,ma.tbody=ma.tfoot=ma.colgroup=ma.caption=ma.thead,ma.th=ma.td;function na(a,b){var c;return c="undefined"!=typeof a.getElementsByTagName?a.getElementsByTagName(b||"*"):"undefined"!=typeof a.querySelectorAll?a.querySelectorAll(b||"*"):[],void 0===b||b&&B(a,b)?r.merge([a],c):c}function oa(a,b){for(var c=0,d=a.length;c<d;c++)W.set(a[c],"globalEval",!b||W.get(b[c],"globalEval"))}var pa=/<|&#?\w+;/;function qa(a,b,c,d,e){for(var f,g,h,i,j,k,l=b.createDocumentFragment(),m=[],n=0,o=a.length;n<o;n++)if(f=a[n],f||0===f)if("object"===r.type(f))r.merge(m,f.nodeType?[f]:f);else if(pa.test(f)){g=g||l.appendChild(b.createElement("div")),h=(ka.exec(f)||["",""])[1].toLowerCase(),i=ma[h]||ma._default,g.innerHTML=i[1]+r.htmlPrefilter(f)+i[2],k=i[0];while(k--)g=g.lastChild;r.merge(m,g.childNodes),g=l.firstChild,g.textContent=""}else m.push(b.createTextNode(f));l.textContent="",n=0;while(f=m[n++])if(d&&r.inArray(f,d)>-1)e&&e.push(f);else if(j=r.contains(f.ownerDocument,f),g=na(l.appendChild(f),"script"),j&&oa(g),c){k=0;while(f=g[k++])la.test(f.type||"")&&c.push(f)}return l}!function(){var a=d.createDocumentFragment(),b=a.appendChild(d.createElement("div")),c=d.createElement("input");c.setAttribute("type","radio"),c.setAttribute("checked","checked"),c.setAttribute("name","t"),b.appendChild(c),o.checkClone=b.cloneNode(!0).cloneNode(!0).lastChild.checked,b.innerHTML="<textarea>x</textarea>",o.noCloneChecked=!!b.cloneNode(!0).lastChild.defaultValue}();var ra=d.documentElement,sa=/^key/,ta=/^(?:mouse|pointer|contextmenu|drag|drop)|click/,ua=/^([^.]*)(?:\.(.+)|)/;function va(){return!0}function wa(){return!1}function xa(){try{return d.activeElement}catch(a){}}function ya(a,b,c,d,e,f){var g,h;if("object"==typeof b){"string"!=typeof c&&(d=d||c,c=void 0);for(h in b)ya(a,h,c,d,b[h],f);return a}if(null==d&&null==e?(e=c,d=c=void 0):null==e&&("string"==typeof c?(e=d,d=void 0):(e=d,d=c,c=void 0)),e===!1)e=wa;else if(!e)return a;return 1===f&&(g=e,e=function(a){return r().off(a),g.apply(this,arguments)},e.guid=g.guid||(g.guid=r.guid++)),a.each(function(){r.event.add(this,b,e,d,c)})}r.event={global:{},add:function(a,b,c,d,e){var f,g,h,i,j,k,l,m,n,o,p,q=W.get(a);if(q){c.handler&&(f=c,c=f.handler,e=f.selector),e&&r.find.matchesSelector(ra,e),c.guid||(c.guid=r.guid++),(i=q.events)||(i=q.events={}),(g=q.handle)||(g=q.handle=function(b){return"undefined"!=typeof r&&r.event.triggered!==b.type?r.event.dispatch.apply(a,arguments):void 0}),b=(b||"").match(L)||[""],j=b.length;while(j--)h=ua.exec(b[j])||[],n=p=h[1],o=(h[2]||"").split(".").sort(),n&&(l=r.event.special[n]||{},n=(e?l.delegateType:l.bindType)||n,l=r.event.special[n]||{},k=r.extend({type:n,origType:p,data:d,handler:c,guid:c.guid,selector:e,needsContext:e&&r.expr.match.needsContext.test(e),namespace:o.join(".")},f),(m=i[n])||(m=i[n]=[],m.delegateCount=0,l.setup&&l.setup.call(a,d,o,g)!==!1||a.addEventListener&&a.addEventListener(n,g)),l.add&&(l.add.call(a,k),k.handler.guid||(k.handler.guid=c.guid)),e?m.splice(m.delegateCount++,0,k):m.push(k),r.event.global[n]=!0)}},remove:function(a,b,c,d,e){var f,g,h,i,j,k,l,m,n,o,p,q=W.hasData(a)&&W.get(a);if(q&&(i=q.events)){b=(b||"").match(L)||[""],j=b.length;while(j--)if(h=ua.exec(b[j])||[],n=p=h[1],o=(h[2]||"").split(".").sort(),n){l=r.event.special[n]||{},n=(d?l.delegateType:l.bindType)||n,m=i[n]||[],h=h[2]&&new RegExp("(^|\\.)"+o.join("\\.(?:.*\\.|)")+"(\\.|$)"),g=f=m.length;while(f--)k=m[f],!e&&p!==k.origType||c&&c.guid!==k.guid||h&&!h.test(k.namespace)||d&&d!==k.selector&&("**"!==d||!k.selector)||(m.splice(f,1),k.selector&&m.delegateCount--,l.remove&&l.remove.call(a,k));g&&!m.length&&(l.teardown&&l.teardown.call(a,o,q.handle)!==!1||r.removeEvent(a,n,q.handle),delete i[n])}else for(n in i)r.event.remove(a,n+b[j],c,d,!0);r.isEmptyObject(i)&&W.remove(a,"handle events")}},dispatch:function(a){var b=r.event.fix(a),c,d,e,f,g,h,i=new Array(arguments.length),j=(W.get(this,"events")||{})[b.type]||[],k=r.event.special[b.type]||{};for(i[0]=b,c=1;c<arguments.length;c++)i[c]=arguments[c];if(b.delegateTarget=this,!k.preDispatch||k.preDispatch.call(this,b)!==!1){h=r.event.handlers.call(this,b,j),c=0;while((f=h[c++])&&!b.isPropagationStopped()){b.currentTarget=f.elem,d=0;while((g=f.handlers[d++])&&!b.isImmediatePropagationStopped())b.rnamespace&&!b.rnamespace.test(g.namespace)||(b.handleObj=g,b.data=g.data,e=((r.event.special[g.origType]||{}).handle||g.handler).apply(f.elem,i),void 0!==e&&(b.result=e)===!1&&(b.preventDefault(),b.stopPropagation()))}return k.postDispatch&&k.postDispatch.call(this,b),b.result}},handlers:function(a,b){var c,d,e,f,g,h=[],i=b.delegateCount,j=a.target;if(i&&j.nodeType&&!("click"===a.type&&a.button>=1))for(;j!==this;j=j.parentNode||this)if(1===j.nodeType&&("click"!==a.type||j.disabled!==!0)){for(f=[],g={},c=0;c<i;c++)d=b[c],e=d.selector+" ",void 0===g[e]&&(g[e]=d.needsContext?r(e,this).index(j)>-1:r.find(e,this,null,[j]).length),g[e]&&f.push(d);f.length&&h.push({elem:j,handlers:f})}return j=this,i<b.length&&h.push({elem:j,handlers:b.slice(i)}),h},addProp:function(a,b){Object.defineProperty(r.Event.prototype,a,{enumerable:!0,configurable:!0,get:r.isFunction(b)?function(){if(this.originalEvent)return b(this.originalEvent)}:function(){if(this.originalEvent)return this.originalEvent[a]},set:function(b){Object.defineProperty(this,a,{enumerable:!0,configurable:!0,writable:!0,value:b})}})},fix:function(a){return a[r.expando]?a:new r.Event(a)},special:{load:{noBubble:!0},focus:{trigger:function(){if(this!==xa()&&this.focus)return this.focus(),!1},delegateType:"focusin"},blur:{trigger:function(){if(this===xa()&&this.blur)return this.blur(),!1},delegateType:"focusout"},click:{trigger:function(){if("checkbox"===this.type&&this.click&&B(this,"input"))return this.click(),!1},_default:function(a){return B(a.target,"a")}},beforeunload:{postDispatch:function(a){void 0!==a.result&&a.originalEvent&&(a.originalEvent.returnValue=a.result)}}}},r.removeEvent=function(a,b,c){a.removeEventListener&&a.removeEventListener(b,c)},r.Event=function(a,b){return this instanceof r.Event?(a&&a.type?(this.originalEvent=a,this.type=a.type,this.isDefaultPrevented=a.defaultPrevented||void 0===a.defaultPrevented&&a.returnValue===!1?va:wa,this.target=a.target&&3===a.target.nodeType?a.target.parentNode:a.target,this.currentTarget=a.currentTarget,this.relatedTarget=a.relatedTarget):this.type=a,b&&r.extend(this,b),this.timeStamp=a&&a.timeStamp||r.now(),void(this[r.expando]=!0)):new r.Event(a,b)},r.Event.prototype={constructor:r.Event,isDefaultPrevented:wa,isPropagationStopped:wa,isImmediatePropagationStopped:wa,isSimulated:!1,preventDefault:function(){var a=this.originalEvent;this.isDefaultPrevented=va,a&&!this.isSimulated&&a.preventDefault()},stopPropagation:function(){var a=this.originalEvent;this.isPropagationStopped=va,a&&!this.isSimulated&&a.stopPropagation()},stopImmediatePropagation:function(){var a=this.originalEvent;this.isImmediatePropagationStopped=va,a&&!this.isSimulated&&a.stopImmediatePropagation(),this.stopPropagation()}},r.each({altKey:!0,bubbles:!0,cancelable:!0,changedTouches:!0,ctrlKey:!0,detail:!0,eventPhase:!0,metaKey:!0,pageX:!0,pageY:!0,shiftKey:!0,view:!0,"char":!0,charCode:!0,key:!0,keyCode:!0,button:!0,buttons:!0,clientX:!0,clientY:!0,offsetX:!0,offsetY:!0,pointerId:!0,pointerType:!0,screenX:!0,screenY:!0,targetTouches:!0,toElement:!0,touches:!0,which:function(a){var b=a.button;return null==a.which&&sa.test(a.type)?null!=a.charCode?a.charCode:a.keyCode:!a.which&&void 0!==b&&ta.test(a.type)?1&b?1:2&b?3:4&b?2:0:a.which}},r.event.addProp),r.each({mouseenter:"mouseover",mouseleave:"mouseout",pointerenter:"pointerover",pointerleave:"pointerout"},function(a,b){r.event.special[a]={delegateType:b,bindType:b,handle:function(a){var c,d=this,e=a.relatedTarget,f=a.handleObj;return e&&(e===d||r.contains(d,e))||(a.type=f.origType,c=f.handler.apply(this,arguments),a.type=b),c}}}),r.fn.extend({on:function(a,b,c,d){return ya(this,a,b,c,d)},one:function(a,b,c,d){return ya(this,a,b,c,d,1)},off:function(a,b,c){var d,e;if(a&&a.preventDefault&&a.handleObj)return d=a.handleObj,r(a.delegateTarget).off(d.namespace?d.origType+"."+d.namespace:d.origType,d.selector,d.handler),this;if("object"==typeof a){for(e in a)this.off(e,b,a[e]);return this}return b!==!1&&"function"!=typeof b||(c=b,b=void 0),c===!1&&(c=wa),this.each(function(){r.event.remove(this,a,c,b)})}});var za=/<(?!area|br|col|embed|hr|img|input|link|meta|param)(([a-z][^\/\0>\x20\t\r\n\f]*)[^>]*)\/>/gi,Aa=/<script|<style|<link/i,Ba=/checked\s*(?:[^=]|=\s*.checked.)/i,Ca=/^true\/(.*)/,Da=/^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g;function Ea(a,b){return B(a,"table")&&B(11!==b.nodeType?b:b.firstChild,"tr")?r(">tbody",a)[0]||a:a}function Fa(a){return a.type=(null!==a.getAttribute("type"))+"/"+a.type,a}function Ga(a){var b=Ca.exec(a.type);return b?a.type=b[1]:a.removeAttribute("type"),a}function Ha(a,b){var c,d,e,f,g,h,i,j;if(1===b.nodeType){if(W.hasData(a)&&(f=W.access(a),g=W.set(b,f),j=f.events)){delete g.handle,g.events={};for(e in j)for(c=0,d=j[e].length;c<d;c++)r.event.add(b,e,j[e][c])}X.hasData(a)&&(h=X.access(a),i=r.extend({},h),X.set(b,i))}}function Ia(a,b){var c=b.nodeName.toLowerCase();"input"===c&&ja.test(a.type)?b.checked=a.checked:"input"!==c&&"textarea"!==c||(b.defaultValue=a.defaultValue)}function Ja(a,b,c,d){b=g.apply([],b);var e,f,h,i,j,k,l=0,m=a.length,n=m-1,q=b[0],s=r.isFunction(q);if(s||m>1&&"string"==typeof q&&!o.checkClone&&Ba.test(q))return a.each(function(e){var f=a.eq(e);s&&(b[0]=q.call(this,e,f.html())),Ja(f,b,c,d)});if(m&&(e=qa(b,a[0].ownerDocument,!1,a,d),f=e.firstChild,1===e.childNodes.length&&(e=f),f||d)){for(h=r.map(na(e,"script"),Fa),i=h.length;l<m;l++)j=e,l!==n&&(j=r.clone(j,!0,!0),i&&r.merge(h,na(j,"script"))),c.call(a[l],j,l);if(i)for(k=h[h.length-1].ownerDocument,r.map(h,Ga),l=0;l<i;l++)j=h[l],la.test(j.type||"")&&!W.access(j,"globalEval")&&r.contains(k,j)&&(j.src?r._evalUrl&&r._evalUrl(j.src):p(j.textContent.replace(Da,""),k))}return a}function Ka(a,b,c){for(var d,e=b?r.filter(b,a):a,f=0;null!=(d=e[f]);f++)c||1!==d.nodeType||r.cleanData(na(d)),d.parentNode&&(c&&r.contains(d.ownerDocument,d)&&oa(na(d,"script")),d.parentNode.removeChild(d));return a}r.extend({htmlPrefilter:function(a){return a.replace(za,"<$1></$2>")},clone:function(a,b,c){var d,e,f,g,h=a.cloneNode(!0),i=r.contains(a.ownerDocument,a);if(!(o.noCloneChecked||1!==a.nodeType&&11!==a.nodeType||r.isXMLDoc(a)))for(g=na(h),f=na(a),d=0,e=f.length;d<e;d++)Ia(f[d],g[d]);if(b)if(c)for(f=f||na(a),g=g||na(h),d=0,e=f.length;d<e;d++)Ha(f[d],g[d]);else Ha(a,h);return g=na(h,"script"),g.length>0&&oa(g,!i&&na(a,"script")),h},cleanData:function(a){for(var b,c,d,e=r.event.special,f=0;void 0!==(c=a[f]);f++)if(U(c)){if(b=c[W.expando]){if(b.events)for(d in b.events)e[d]?r.event.remove(c,d):r.removeEvent(c,d,b.handle);c[W.expando]=void 0}c[X.expando]&&(c[X.expando]=void 0)}}}),r.fn.extend({detach:function(a){return Ka(this,a,!0)},remove:function(a){return Ka(this,a)},text:function(a){return T(this,function(a){return void 0===a?r.text(this):this.empty().each(function(){1!==this.nodeType&&11!==this.nodeType&&9!==this.nodeType||(this.textContent=a)})},null,a,arguments.length)},append:function(){return Ja(this,arguments,function(a){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var b=Ea(this,a);b.appendChild(a)}})},prepend:function(){return Ja(this,arguments,function(a){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var b=Ea(this,a);b.insertBefore(a,b.firstChild)}})},before:function(){return Ja(this,arguments,function(a){this.parentNode&&this.parentNode.insertBefore(a,this)})},after:function(){return Ja(this,arguments,function(a){this.parentNode&&this.parentNode.insertBefore(a,this.nextSibling)})},empty:function(){for(var a,b=0;null!=(a=this[b]);b++)1===a.nodeType&&(r.cleanData(na(a,!1)),a.textContent="");return this},clone:function(a,b){return a=null!=a&&a,b=null==b?a:b,this.map(function(){return r.clone(this,a,b)})},html:function(a){return T(this,function(a){var b=this[0]||{},c=0,d=this.length;if(void 0===a&&1===b.nodeType)return b.innerHTML;if("string"==typeof a&&!Aa.test(a)&&!ma[(ka.exec(a)||["",""])[1].toLowerCase()]){a=r.htmlPrefilter(a);try{for(;c<d;c++)b=this[c]||{},1===b.nodeType&&(r.cleanData(na(b,!1)),b.innerHTML=a);b=0}catch(e){}}b&&this.empty().append(a)},null,a,arguments.length)},replaceWith:function(){var a=[];return Ja(this,arguments,function(b){var c=this.parentNode;r.inArray(this,a)<0&&(r.cleanData(na(this)),c&&c.replaceChild(b,this))},a)}}),r.each({appendTo:"append",prependTo:"prepend",insertBefore:"before",insertAfter:"after",replaceAll:"replaceWith"},function(a,b){r.fn[a]=function(a){for(var c,d=[],e=r(a),f=e.length-1,g=0;g<=f;g++)c=g===f?this:this.clone(!0),r(e[g])[b](c),h.apply(d,c.get());return this.pushStack(d)}});var La=/^margin/,Ma=new RegExp("^("+aa+")(?!px)[a-z%]+$","i"),Na=function(b){var c=b.ownerDocument.defaultView;return c&&c.opener||(c=a),c.getComputedStyle(b)};!function(){function b(){if(i){i.style.cssText="box-sizing:border-box;position:relative;display:block;margin:auto;border:1px;padding:1px;top:1%;width:50%",i.innerHTML="",ra.appendChild(h);var b=a.getComputedStyle(i);c="1%"!==b.top,g="2px"===b.marginLeft,e="4px"===b.width,i.style.marginRight="50%",f="4px"===b.marginRight,ra.removeChild(h),i=null}}var c,e,f,g,h=d.createElement("div"),i=d.createElement("div");i.style&&(i.style.backgroundClip="content-box",i.cloneNode(!0).style.backgroundClip="",o.clearCloneStyle="content-box"===i.style.backgroundClip,h.style.cssText="border:0;width:8px;height:0;top:0;left:-9999px;padding:0;margin-top:1px;position:absolute",h.appendChild(i),r.extend(o,{pixelPosition:function(){return b(),c},boxSizingReliable:function(){return b(),e},pixelMarginRight:function(){return b(),f},reliableMarginLeft:function(){return b(),g}}))}();function Oa(a,b,c){var d,e,f,g,h=a.style;return c=c||Na(a),c&&(g=c.getPropertyValue(b)||c[b],""!==g||r.contains(a.ownerDocument,a)||(g=r.style(a,b)),!o.pixelMarginRight()&&Ma.test(g)&&La.test(b)&&(d=h.width,e=h.minWidth,f=h.maxWidth,h.minWidth=h.maxWidth=h.width=g,g=c.width,h.width=d,h.minWidth=e,h.maxWidth=f)),void 0!==g?g+"":g}function Pa(a,b){return{get:function(){return a()?void delete this.get:(this.get=b).apply(this,arguments)}}}var Qa=/^(none|table(?!-c[ea]).+)/,Ra=/^--/,Sa={position:"absolute",visibility:"hidden",display:"block"},Ta={letterSpacing:"0",fontWeight:"400"},Ua=["Webkit","Moz","ms"],Va=d.createElement("div").style;function Wa(a){if(a in Va)return a;var b=a[0].toUpperCase()+a.slice(1),c=Ua.length;while(c--)if(a=Ua[c]+b,a in Va)return a}function Xa(a){var b=r.cssProps[a];return b||(b=r.cssProps[a]=Wa(a)||a),b}function Ya(a,b,c){var d=ba.exec(b);return d?Math.max(0,d[2]-(c||0))+(d[3]||"px"):b}function Za(a,b,c,d,e){var f,g=0;for(f=c===(d?"border":"content")?4:"width"===b?1:0;f<4;f+=2)"margin"===c&&(g+=r.css(a,c+ca[f],!0,e)),d?("content"===c&&(g-=r.css(a,"padding"+ca[f],!0,e)),"margin"!==c&&(g-=r.css(a,"border"+ca[f]+"Width",!0,e))):(g+=r.css(a,"padding"+ca[f],!0,e),"padding"!==c&&(g+=r.css(a,"border"+ca[f]+"Width",!0,e)));return g}function $a(a,b,c){var d,e=Na(a),f=Oa(a,b,e),g="border-box"===r.css(a,"boxSizing",!1,e);return Ma.test(f)?f:(d=g&&(o.boxSizingReliable()||f===a.style[b]),"auto"===f&&(f=a["offset"+b[0].toUpperCase()+b.slice(1)]),f=parseFloat(f)||0,f+Za(a,b,c||(g?"border":"content"),d,e)+"px")}r.extend({cssHooks:{opacity:{get:function(a,b){if(b){var c=Oa(a,"opacity");return""===c?"1":c}}}},cssNumber:{animationIterationCount:!0,columnCount:!0,fillOpacity:!0,flexGrow:!0,flexShrink:!0,fontWeight:!0,lineHeight:!0,opacity:!0,order:!0,orphans:!0,widows:!0,zIndex:!0,zoom:!0},cssProps:{"float":"cssFloat"},style:function(a,b,c,d){if(a&&3!==a.nodeType&&8!==a.nodeType&&a.style){var e,f,g,h=r.camelCase(b),i=Ra.test(b),j=a.style;return i||(b=Xa(h)),g=r.cssHooks[b]||r.cssHooks[h],void 0===c?g&&"get"in g&&void 0!==(e=g.get(a,!1,d))?e:j[b]:(f=typeof c,"string"===f&&(e=ba.exec(c))&&e[1]&&(c=fa(a,b,e),f="number"),null!=c&&c===c&&("number"===f&&(c+=e&&e[3]||(r.cssNumber[h]?"":"px")),o.clearCloneStyle||""!==c||0!==b.indexOf("background")||(j[b]="inherit"),g&&"set"in g&&void 0===(c=g.set(a,c,d))||(i?j.setProperty(b,c):j[b]=c)),void 0)}},css:function(a,b,c,d){var e,f,g,h=r.camelCase(b),i=Ra.test(b);return i||(b=Xa(h)),g=r.cssHooks[b]||r.cssHooks[h],g&&"get"in g&&(e=g.get(a,!0,c)),void 0===e&&(e=Oa(a,b,d)),"normal"===e&&b in Ta&&(e=Ta[b]),""===c||c?(f=parseFloat(e),c===!0||isFinite(f)?f||0:e):e}}),r.each(["height","width"],function(a,b){r.cssHooks[b]={get:function(a,c,d){if(c)return!Qa.test(r.css(a,"display"))||a.getClientRects().length&&a.getBoundingClientRect().width?$a(a,b,d):ea(a,Sa,function(){return $a(a,b,d)})},set:function(a,c,d){var e,f=d&&Na(a),g=d&&Za(a,b,d,"border-box"===r.css(a,"boxSizing",!1,f),f);return g&&(e=ba.exec(c))&&"px"!==(e[3]||"px")&&(a.style[b]=c,c=r.css(a,b)),Ya(a,c,g)}}}),r.cssHooks.marginLeft=Pa(o.reliableMarginLeft,function(a,b){if(b)return(parseFloat(Oa(a,"marginLeft"))||a.getBoundingClientRect().left-ea(a,{marginLeft:0},function(){return a.getBoundingClientRect().left}))+"px"}),r.each({margin:"",padding:"",border:"Width"},function(a,b){r.cssHooks[a+b]={expand:function(c){for(var d=0,e={},f="string"==typeof c?c.split(" "):[c];d<4;d++)e[a+ca[d]+b]=f[d]||f[d-2]||f[0];return e}},La.test(a)||(r.cssHooks[a+b].set=Ya)}),r.fn.extend({css:function(a,b){return T(this,function(a,b,c){var d,e,f={},g=0;if(Array.isArray(b)){for(d=Na(a),e=b.length;g<e;g++)f[b[g]]=r.css(a,b[g],!1,d);return f}return void 0!==c?r.style(a,b,c):r.css(a,b)},a,b,arguments.length>1)}});function _a(a,b,c,d,e){return new _a.prototype.init(a,b,c,d,e)}r.Tween=_a,_a.prototype={constructor:_a,init:function(a,b,c,d,e,f){this.elem=a,this.prop=c,this.easing=e||r.easing._default,this.options=b,this.start=this.now=this.cur(),this.end=d,this.unit=f||(r.cssNumber[c]?"":"px")},cur:function(){var a=_a.propHooks[this.prop];return a&&a.get?a.get(this):_a.propHooks._default.get(this)},run:function(a){var b,c=_a.propHooks[this.prop];return this.options.duration?this.pos=b=r.easing[this.easing](a,this.options.duration*a,0,1,this.options.duration):this.pos=b=a,this.now=(this.end-this.start)*b+this.start,this.options.step&&this.options.step.call(this.elem,this.now,this),c&&c.set?c.set(this):_a.propHooks._default.set(this),this}},_a.prototype.init.prototype=_a.prototype,_a.propHooks={_default:{get:function(a){var b;return 1!==a.elem.nodeType||null!=a.elem[a.prop]&&null==a.elem.style[a.prop]?a.elem[a.prop]:(b=r.css(a.elem,a.prop,""),b&&"auto"!==b?b:0)},set:function(a){r.fx.step[a.prop]?r.fx.step[a.prop](a):1!==a.elem.nodeType||null==a.elem.style[r.cssProps[a.prop]]&&!r.cssHooks[a.prop]?a.elem[a.prop]=a.now:r.style(a.elem,a.prop,a.now+a.unit)}}},_a.propHooks.scrollTop=_a.propHooks.scrollLeft={set:function(a){a.elem.nodeType&&a.elem.parentNode&&(a.elem[a.prop]=a.now)}},r.easing={linear:function(a){return a},swing:function(a){return.5-Math.cos(a*Math.PI)/2},_default:"swing"},r.fx=_a.prototype.init,r.fx.step={};var ab,bb,cb=/^(?:toggle|show|hide)$/,db=/queueHooks$/;function eb(){bb&&(d.hidden===!1&&a.requestAnimationFrame?a.requestAnimationFrame(eb):a.setTimeout(eb,r.fx.interval),r.fx.tick())}function fb(){return a.setTimeout(function(){ab=void 0}),ab=r.now()}function gb(a,b){var c,d=0,e={height:a};for(b=b?1:0;d<4;d+=2-b)c=ca[d],e["margin"+c]=e["padding"+c]=a;return b&&(e.opacity=e.width=a),e}function hb(a,b,c){for(var d,e=(kb.tweeners[b]||[]).concat(kb.tweeners["*"]),f=0,g=e.length;f<g;f++)if(d=e[f].call(c,b,a))return d}function ib(a,b,c){var d,e,f,g,h,i,j,k,l="width"in b||"height"in b,m=this,n={},o=a.style,p=a.nodeType&&da(a),q=W.get(a,"fxshow");c.queue||(g=r._queueHooks(a,"fx"),null==g.unqueued&&(g.unqueued=0,h=g.empty.fire,g.empty.fire=function(){g.unqueued||h()}),g.unqueued++,m.always(function(){m.always(function(){g.unqueued--,r.queue(a,"fx").length||g.empty.fire()})}));for(d in b)if(e=b[d],cb.test(e)){if(delete b[d],f=f||"toggle"===e,e===(p?"hide":"show")){if("show"!==e||!q||void 0===q[d])continue;p=!0}n[d]=q&&q[d]||r.style(a,d)}if(i=!r.isEmptyObject(b),i||!r.isEmptyObject(n)){l&&1===a.nodeType&&(c.overflow=[o.overflow,o.overflowX,o.overflowY],j=q&&q.display,null==j&&(j=W.get(a,"display")),k=r.css(a,"display"),"none"===k&&(j?k=j:(ia([a],!0),j=a.style.display||j,k=r.css(a,"display"),ia([a]))),("inline"===k||"inline-block"===k&&null!=j)&&"none"===r.css(a,"float")&&(i||(m.done(function(){o.display=j}),null==j&&(k=o.display,j="none"===k?"":k)),o.display="inline-block")),c.overflow&&(o.overflow="hidden",m.always(function(){o.overflow=c.overflow[0],o.overflowX=c.overflow[1],o.overflowY=c.overflow[2]})),i=!1;for(d in n)i||(q?"hidden"in q&&(p=q.hidden):q=W.access(a,"fxshow",{display:j}),f&&(q.hidden=!p),p&&ia([a],!0),m.done(function(){p||ia([a]),W.remove(a,"fxshow");for(d in n)r.style(a,d,n[d])})),i=hb(p?q[d]:0,d,m),d in q||(q[d]=i.start,p&&(i.end=i.start,i.start=0))}}function jb(a,b){var c,d,e,f,g;for(c in a)if(d=r.camelCase(c),e=b[d],f=a[c],Array.isArray(f)&&(e=f[1],f=a[c]=f[0]),c!==d&&(a[d]=f,delete a[c]),g=r.cssHooks[d],g&&"expand"in g){f=g.expand(f),delete a[d];for(c in f)c in a||(a[c]=f[c],b[c]=e)}else b[d]=e}function kb(a,b,c){var d,e,f=0,g=kb.prefilters.length,h=r.Deferred().always(function(){delete i.elem}),i=function(){if(e)return!1;for(var b=ab||fb(),c=Math.max(0,j.startTime+j.duration-b),d=c/j.duration||0,f=1-d,g=0,i=j.tweens.length;g<i;g++)j.tweens[g].run(f);return h.notifyWith(a,[j,f,c]),f<1&&i?c:(i||h.notifyWith(a,[j,1,0]),h.resolveWith(a,[j]),!1)},j=h.promise({elem:a,props:r.extend({},b),opts:r.extend(!0,{specialEasing:{},easing:r.easing._default},c),originalProperties:b,originalOptions:c,startTime:ab||fb(),duration:c.duration,tweens:[],createTween:function(b,c){var d=r.Tween(a,j.opts,b,c,j.opts.specialEasing[b]||j.opts.easing);return j.tweens.push(d),d},stop:function(b){var c=0,d=b?j.tweens.length:0;if(e)return this;for(e=!0;c<d;c++)j.tweens[c].run(1);return b?(h.notifyWith(a,[j,1,0]),h.resolveWith(a,[j,b])):h.rejectWith(a,[j,b]),this}}),k=j.props;for(jb(k,j.opts.specialEasing);f<g;f++)if(d=kb.prefilters[f].call(j,a,k,j.opts))return r.isFunction(d.stop)&&(r._queueHooks(j.elem,j.opts.queue).stop=r.proxy(d.stop,d)),d;return r.map(k,hb,j),r.isFunction(j.opts.start)&&j.opts.start.call(a,j),j.progress(j.opts.progress).done(j.opts.done,j.opts.complete).fail(j.opts.fail).always(j.opts.always),r.fx.timer(r.extend(i,{elem:a,anim:j,queue:j.opts.queue})),j}r.Animation=r.extend(kb,{tweeners:{"*":[function(a,b){var c=this.createTween(a,b);return fa(c.elem,a,ba.exec(b),c),c}]},tweener:function(a,b){r.isFunction(a)?(b=a,a=["*"]):a=a.match(L);for(var c,d=0,e=a.length;d<e;d++)c=a[d],kb.tweeners[c]=kb.tweeners[c]||[],kb.tweeners[c].unshift(b)},prefilters:[ib],prefilter:function(a,b){b?kb.prefilters.unshift(a):kb.prefilters.push(a)}}),r.speed=function(a,b,c){var d=a&&"object"==typeof a?r.extend({},a):{complete:c||!c&&b||r.isFunction(a)&&a,duration:a,easing:c&&b||b&&!r.isFunction(b)&&b};return r.fx.off?d.duration=0:"number"!=typeof d.duration&&(d.duration in r.fx.speeds?d.duration=r.fx.speeds[d.duration]:d.duration=r.fx.speeds._default),null!=d.queue&&d.queue!==!0||(d.queue="fx"),d.old=d.complete,d.complete=function(){r.isFunction(d.old)&&d.old.call(this),d.queue&&r.dequeue(this,d.queue)},d},r.fn.extend({fadeTo:function(a,b,c,d){return this.filter(da).css("opacity",0).show().end().animate({opacity:b},a,c,d)},animate:function(a,b,c,d){var e=r.isEmptyObject(a),f=r.speed(b,c,d),g=function(){var b=kb(this,r.extend({},a),f);(e||W.get(this,"finish"))&&b.stop(!0)};return g.finish=g,e||f.queue===!1?this.each(g):this.queue(f.queue,g)},stop:function(a,b,c){var d=function(a){var b=a.stop;delete a.stop,b(c)};return"string"!=typeof a&&(c=b,b=a,a=void 0),b&&a!==!1&&this.queue(a||"fx",[]),this.each(function(){var b=!0,e=null!=a&&a+"queueHooks",f=r.timers,g=W.get(this);if(e)g[e]&&g[e].stop&&d(g[e]);else for(e in g)g[e]&&g[e].stop&&db.test(e)&&d(g[e]);for(e=f.length;e--;)f[e].elem!==this||null!=a&&f[e].queue!==a||(f[e].anim.stop(c),b=!1,f.splice(e,1));!b&&c||r.dequeue(this,a)})},finish:function(a){return a!==!1&&(a=a||"fx"),this.each(function(){var b,c=W.get(this),d=c[a+"queue"],e=c[a+"queueHooks"],f=r.timers,g=d?d.length:0;for(c.finish=!0,r.queue(this,a,[]),e&&e.stop&&e.stop.call(this,!0),b=f.length;b--;)f[b].elem===this&&f[b].queue===a&&(f[b].anim.stop(!0),f.splice(b,1));for(b=0;b<g;b++)d[b]&&d[b].finish&&d[b].finish.call(this);delete c.finish})}}),r.each(["toggle","show","hide"],function(a,b){var c=r.fn[b];r.fn[b]=function(a,d,e){return null==a||"boolean"==typeof a?c.apply(this,arguments):this.animate(gb(b,!0),a,d,e)}}),r.each({slideDown:gb("show"),slideUp:gb("hide"),slideToggle:gb("toggle"),fadeIn:{opacity:"show"},fadeOut:{opacity:"hide"},fadeToggle:{opacity:"toggle"}},function(a,b){r.fn[a]=function(a,c,d){return this.animate(b,a,c,d)}}),r.timers=[],r.fx.tick=function(){var a,b=0,c=r.timers;for(ab=r.now();b<c.length;b++)a=c[b],a()||c[b]!==a||c.splice(b--,1);c.length||r.fx.stop(),ab=void 0},r.fx.timer=function(a){r.timers.push(a),r.fx.start()},r.fx.interval=13,r.fx.start=function(){bb||(bb=!0,eb())},r.fx.stop=function(){bb=null},r.fx.speeds={slow:600,fast:200,_default:400},r.fn.delay=function(b,c){return b=r.fx?r.fx.speeds[b]||b:b,c=c||"fx",this.queue(c,function(c,d){var e=a.setTimeout(c,b);d.stop=function(){a.clearTimeout(e)}})},function(){var a=d.createElement("input"),b=d.createElement("select"),c=b.appendChild(d.createElement("option"));a.type="checkbox",o.checkOn=""!==a.value,o.optSelected=c.selected,a=d.createElement("input"),a.value="t",a.type="radio",o.radioValue="t"===a.value}();var lb,mb=r.expr.attrHandle;r.fn.extend({attr:function(a,b){return T(this,r.attr,a,b,arguments.length>1)},removeAttr:function(a){return this.each(function(){r.removeAttr(this,a)})}}),r.extend({attr:function(a,b,c){var d,e,f=a.nodeType;if(3!==f&&8!==f&&2!==f)return"undefined"==typeof a.getAttribute?r.prop(a,b,c):(1===f&&r.isXMLDoc(a)||(e=r.attrHooks[b.toLowerCase()]||(r.expr.match.bool.test(b)?lb:void 0)),void 0!==c?null===c?void r.removeAttr(a,b):e&&"set"in e&&void 0!==(d=e.set(a,c,b))?d:(a.setAttribute(b,c+""),c):e&&"get"in e&&null!==(d=e.get(a,b))?d:(d=r.find.attr(a,b),
    null==d?void 0:d))},attrHooks:{type:{set:function(a,b){if(!o.radioValue&&"radio"===b&&B(a,"input")){var c=a.value;return a.setAttribute("type",b),c&&(a.value=c),b}}}},removeAttr:function(a,b){var c,d=0,e=b&&b.match(L);if(e&&1===a.nodeType)while(c=e[d++])a.removeAttribute(c)}}),lb={set:function(a,b,c){return b===!1?r.removeAttr(a,c):a.setAttribute(c,c),c}},r.each(r.expr.match.bool.source.match(/\w+/g),function(a,b){var c=mb[b]||r.find.attr;mb[b]=function(a,b,d){var e,f,g=b.toLowerCase();return d||(f=mb[g],mb[g]=e,e=null!=c(a,b,d)?g:null,mb[g]=f),e}});var nb=/^(?:input|select|textarea|button)$/i,ob=/^(?:a|area)$/i;r.fn.extend({prop:function(a,b){return T(this,r.prop,a,b,arguments.length>1)},removeProp:function(a){return this.each(function(){delete this[r.propFix[a]||a]})}}),r.extend({prop:function(a,b,c){var d,e,f=a.nodeType;if(3!==f&&8!==f&&2!==f)return 1===f&&r.isXMLDoc(a)||(b=r.propFix[b]||b,e=r.propHooks[b]),void 0!==c?e&&"set"in e&&void 0!==(d=e.set(a,c,b))?d:a[b]=c:e&&"get"in e&&null!==(d=e.get(a,b))?d:a[b]},propHooks:{tabIndex:{get:function(a){var b=r.find.attr(a,"tabindex");return b?parseInt(b,10):nb.test(a.nodeName)||ob.test(a.nodeName)&&a.href?0:-1}}},propFix:{"for":"htmlFor","class":"className"}}),o.optSelected||(r.propHooks.selected={get:function(a){var b=a.parentNode;return b&&b.parentNode&&b.parentNode.selectedIndex,null},set:function(a){var b=a.parentNode;b&&(b.selectedIndex,b.parentNode&&b.parentNode.selectedIndex)}}),r.each(["tabIndex","readOnly","maxLength","cellSpacing","cellPadding","rowSpan","colSpan","useMap","frameBorder","contentEditable"],function(){r.propFix[this.toLowerCase()]=this});function pb(a){var b=a.match(L)||[];return b.join(" ")}function qb(a){return a.getAttribute&&a.getAttribute("class")||""}r.fn.extend({addClass:function(a){var b,c,d,e,f,g,h,i=0;if(r.isFunction(a))return this.each(function(b){r(this).addClass(a.call(this,b,qb(this)))});if("string"==typeof a&&a){b=a.match(L)||[];while(c=this[i++])if(e=qb(c),d=1===c.nodeType&&" "+pb(e)+" "){g=0;while(f=b[g++])d.indexOf(" "+f+" ")<0&&(d+=f+" ");h=pb(d),e!==h&&c.setAttribute("class",h)}}return this},removeClass:function(a){var b,c,d,e,f,g,h,i=0;if(r.isFunction(a))return this.each(function(b){r(this).removeClass(a.call(this,b,qb(this)))});if(!arguments.length)return this.attr("class","");if("string"==typeof a&&a){b=a.match(L)||[];while(c=this[i++])if(e=qb(c),d=1===c.nodeType&&" "+pb(e)+" "){g=0;while(f=b[g++])while(d.indexOf(" "+f+" ")>-1)d=d.replace(" "+f+" "," ");h=pb(d),e!==h&&c.setAttribute("class",h)}}return this},toggleClass:function(a,b){var c=typeof a;return"boolean"==typeof b&&"string"===c?b?this.addClass(a):this.removeClass(a):r.isFunction(a)?this.each(function(c){r(this).toggleClass(a.call(this,c,qb(this),b),b)}):this.each(function(){var b,d,e,f;if("string"===c){d=0,e=r(this),f=a.match(L)||[];while(b=f[d++])e.hasClass(b)?e.removeClass(b):e.addClass(b)}else void 0!==a&&"boolean"!==c||(b=qb(this),b&&W.set(this,"__className__",b),this.setAttribute&&this.setAttribute("class",b||a===!1?"":W.get(this,"__className__")||""))})},hasClass:function(a){var b,c,d=0;b=" "+a+" ";while(c=this[d++])if(1===c.nodeType&&(" "+pb(qb(c))+" ").indexOf(b)>-1)return!0;return!1}});var rb=/\r/g;r.fn.extend({val:function(a){var b,c,d,e=this[0];{if(arguments.length)return d=r.isFunction(a),this.each(function(c){var e;1===this.nodeType&&(e=d?a.call(this,c,r(this).val()):a,null==e?e="":"number"==typeof e?e+="":Array.isArray(e)&&(e=r.map(e,function(a){return null==a?"":a+""})),b=r.valHooks[this.type]||r.valHooks[this.nodeName.toLowerCase()],b&&"set"in b&&void 0!==b.set(this,e,"value")||(this.value=e))});if(e)return b=r.valHooks[e.type]||r.valHooks[e.nodeName.toLowerCase()],b&&"get"in b&&void 0!==(c=b.get(e,"value"))?c:(c=e.value,"string"==typeof c?c.replace(rb,""):null==c?"":c)}}}),r.extend({valHooks:{option:{get:function(a){var b=r.find.attr(a,"value");return null!=b?b:pb(r.text(a))}},select:{get:function(a){var b,c,d,e=a.options,f=a.selectedIndex,g="select-one"===a.type,h=g?null:[],i=g?f+1:e.length;for(d=f<0?i:g?f:0;d<i;d++)if(c=e[d],(c.selected||d===f)&&!c.disabled&&(!c.parentNode.disabled||!B(c.parentNode,"optgroup"))){if(b=r(c).val(),g)return b;h.push(b)}return h},set:function(a,b){var c,d,e=a.options,f=r.makeArray(b),g=e.length;while(g--)d=e[g],(d.selected=r.inArray(r.valHooks.option.get(d),f)>-1)&&(c=!0);return c||(a.selectedIndex=-1),f}}}}),r.each(["radio","checkbox"],function(){r.valHooks[this]={set:function(a,b){if(Array.isArray(b))return a.checked=r.inArray(r(a).val(),b)>-1}},o.checkOn||(r.valHooks[this].get=function(a){return null===a.getAttribute("value")?"on":a.value})});var sb=/^(?:focusinfocus|focusoutblur)$/;r.extend(r.event,{trigger:function(b,c,e,f){var g,h,i,j,k,m,n,o=[e||d],p=l.call(b,"type")?b.type:b,q=l.call(b,"namespace")?b.namespace.split("."):[];if(h=i=e=e||d,3!==e.nodeType&&8!==e.nodeType&&!sb.test(p+r.event.triggered)&&(p.indexOf(".")>-1&&(q=p.split("."),p=q.shift(),q.sort()),k=p.indexOf(":")<0&&"on"+p,b=b[r.expando]?b:new r.Event(p,"object"==typeof b&&b),b.isTrigger=f?2:3,b.namespace=q.join("."),b.rnamespace=b.namespace?new RegExp("(^|\\.)"+q.join("\\.(?:.*\\.|)")+"(\\.|$)"):null,b.result=void 0,b.target||(b.target=e),c=null==c?[b]:r.makeArray(c,[b]),n=r.event.special[p]||{},f||!n.trigger||n.trigger.apply(e,c)!==!1)){if(!f&&!n.noBubble&&!r.isWindow(e)){for(j=n.delegateType||p,sb.test(j+p)||(h=h.parentNode);h;h=h.parentNode)o.push(h),i=h;i===(e.ownerDocument||d)&&o.push(i.defaultView||i.parentWindow||a)}g=0;while((h=o[g++])&&!b.isPropagationStopped())b.type=g>1?j:n.bindType||p,m=(W.get(h,"events")||{})[b.type]&&W.get(h,"handle"),m&&m.apply(h,c),m=k&&h[k],m&&m.apply&&U(h)&&(b.result=m.apply(h,c),b.result===!1&&b.preventDefault());return b.type=p,f||b.isDefaultPrevented()||n._default&&n._default.apply(o.pop(),c)!==!1||!U(e)||k&&r.isFunction(e[p])&&!r.isWindow(e)&&(i=e[k],i&&(e[k]=null),r.event.triggered=p,e[p](),r.event.triggered=void 0,i&&(e[k]=i)),b.result}},simulate:function(a,b,c){var d=r.extend(new r.Event,c,{type:a,isSimulated:!0});r.event.trigger(d,null,b)}}),r.fn.extend({trigger:function(a,b){return this.each(function(){r.event.trigger(a,b,this)})},triggerHandler:function(a,b){var c=this[0];if(c)return r.event.trigger(a,b,c,!0)}}),r.each("blur focus focusin focusout resize scroll click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup contextmenu".split(" "),function(a,b){r.fn[b]=function(a,c){return arguments.length>0?this.on(b,null,a,c):this.trigger(b)}}),r.fn.extend({hover:function(a,b){return this.mouseenter(a).mouseleave(b||a)}}),o.focusin="onfocusin"in a,o.focusin||r.each({focus:"focusin",blur:"focusout"},function(a,b){var c=function(a){r.event.simulate(b,a.target,r.event.fix(a))};r.event.special[b]={setup:function(){var d=this.ownerDocument||this,e=W.access(d,b);e||d.addEventListener(a,c,!0),W.access(d,b,(e||0)+1)},teardown:function(){var d=this.ownerDocument||this,e=W.access(d,b)-1;e?W.access(d,b,e):(d.removeEventListener(a,c,!0),W.remove(d,b))}}});var tb=a.location,ub=r.now(),vb=/\?/;r.parseXML=function(b){var c;if(!b||"string"!=typeof b)return null;try{c=(new a.DOMParser).parseFromString(b,"text/xml")}catch(d){c=void 0}return c&&!c.getElementsByTagName("parsererror").length||r.error("Invalid XML: "+b),c};var wb=/\[\]$/,xb=/\r?\n/g,yb=/^(?:submit|button|image|reset|file)$/i,zb=/^(?:input|select|textarea|keygen)/i;function Ab(a,b,c,d){var e;if(Array.isArray(b))r.each(b,function(b,e){c||wb.test(a)?d(a,e):Ab(a+"["+("object"==typeof e&&null!=e?b:"")+"]",e,c,d)});else if(c||"object"!==r.type(b))d(a,b);else for(e in b)Ab(a+"["+e+"]",b[e],c,d)}r.param=function(a,b){var c,d=[],e=function(a,b){var c=r.isFunction(b)?b():b;d[d.length]=encodeURIComponent(a)+"="+encodeURIComponent(null==c?"":c)};if(Array.isArray(a)||a.jquery&&!r.isPlainObject(a))r.each(a,function(){e(this.name,this.value)});else for(c in a)Ab(c,a[c],b,e);return d.join("&")},r.fn.extend({serialize:function(){return r.param(this.serializeArray())},serializeArray:function(){return this.map(function(){var a=r.prop(this,"elements");return a?r.makeArray(a):this}).filter(function(){var a=this.type;return this.name&&!r(this).is(":disabled")&&zb.test(this.nodeName)&&!yb.test(a)&&(this.checked||!ja.test(a))}).map(function(a,b){var c=r(this).val();return null==c?null:Array.isArray(c)?r.map(c,function(a){return{name:b.name,value:a.replace(xb,"\r\n")}}):{name:b.name,value:c.replace(xb,"\r\n")}}).get()}});var Bb=/%20/g,Cb=/#.*$/,Db=/([?&])_=[^&]*/,Eb=/^(.*?):[ \t]*([^\r\n]*)$/gm,Fb=/^(?:about|app|app-storage|.+-extension|file|res|widget):$/,Gb=/^(?:GET|HEAD)$/,Hb=/^\/\//,Ib={},Jb={},Kb="*/".concat("*"),Lb=d.createElement("a");Lb.href=tb.href;function Mb(a){return function(b,c){"string"!=typeof b&&(c=b,b="*");var d,e=0,f=b.toLowerCase().match(L)||[];if(r.isFunction(c))while(d=f[e++])"+"===d[0]?(d=d.slice(1)||"*",(a[d]=a[d]||[]).unshift(c)):(a[d]=a[d]||[]).push(c)}}function Nb(a,b,c,d){var e={},f=a===Jb;function g(h){var i;return e[h]=!0,r.each(a[h]||[],function(a,h){var j=h(b,c,d);return"string"!=typeof j||f||e[j]?f?!(i=j):void 0:(b.dataTypes.unshift(j),g(j),!1)}),i}return g(b.dataTypes[0])||!e["*"]&&g("*")}function Ob(a,b){var c,d,e=r.ajaxSettings.flatOptions||{};for(c in b)void 0!==b[c]&&((e[c]?a:d||(d={}))[c]=b[c]);return d&&r.extend(!0,a,d),a}function Pb(a,b,c){var d,e,f,g,h=a.contents,i=a.dataTypes;while("*"===i[0])i.shift(),void 0===d&&(d=a.mimeType||b.getResponseHeader("Content-Type"));if(d)for(e in h)if(h[e]&&h[e].test(d)){i.unshift(e);break}if(i[0]in c)f=i[0];else{for(e in c){if(!i[0]||a.converters[e+" "+i[0]]){f=e;break}g||(g=e)}f=f||g}if(f)return f!==i[0]&&i.unshift(f),c[f]}function Qb(a,b,c,d){var e,f,g,h,i,j={},k=a.dataTypes.slice();if(k[1])for(g in a.converters)j[g.toLowerCase()]=a.converters[g];f=k.shift();while(f)if(a.responseFields[f]&&(c[a.responseFields[f]]=b),!i&&d&&a.dataFilter&&(b=a.dataFilter(b,a.dataType)),i=f,f=k.shift())if("*"===f)f=i;else if("*"!==i&&i!==f){if(g=j[i+" "+f]||j["* "+f],!g)for(e in j)if(h=e.split(" "),h[1]===f&&(g=j[i+" "+h[0]]||j["* "+h[0]])){g===!0?g=j[e]:j[e]!==!0&&(f=h[0],k.unshift(h[1]));break}if(g!==!0)if(g&&a["throws"])b=g(b);else try{b=g(b)}catch(l){return{state:"parsererror",error:g?l:"No conversion from "+i+" to "+f}}}return{state:"success",data:b}}r.extend({active:0,lastModified:{},etag:{},ajaxSettings:{url:tb.href,type:"GET",isLocal:Fb.test(tb.protocol),global:!0,processData:!0,async:!0,contentType:"application/x-www-form-urlencoded; charset=UTF-8",accepts:{"*":Kb,text:"text/plain",html:"text/html",xml:"application/xml, text/xml",json:"application/json, text/javascript"},contents:{xml:/\bxml\b/,html:/\bhtml/,json:/\bjson\b/},responseFields:{xml:"responseXML",text:"responseText",json:"responseJSON"},converters:{"* text":String,"text html":!0,"text json":JSON.parse,"text xml":r.parseXML},flatOptions:{url:!0,context:!0}},ajaxSetup:function(a,b){return b?Ob(Ob(a,r.ajaxSettings),b):Ob(r.ajaxSettings,a)},ajaxPrefilter:Mb(Ib),ajaxTransport:Mb(Jb),ajax:function(b,c){"object"==typeof b&&(c=b,b=void 0),c=c||{};var e,f,g,h,i,j,k,l,m,n,o=r.ajaxSetup({},c),p=o.context||o,q=o.context&&(p.nodeType||p.jquery)?r(p):r.event,s=r.Deferred(),t=r.Callbacks("once memory"),u=o.statusCode||{},v={},w={},x="canceled",y={readyState:0,getResponseHeader:function(a){var b;if(k){if(!h){h={};while(b=Eb.exec(g))h[b[1].toLowerCase()]=b[2]}b=h[a.toLowerCase()]}return null==b?null:b},getAllResponseHeaders:function(){return k?g:null},setRequestHeader:function(a,b){return null==k&&(a=w[a.toLowerCase()]=w[a.toLowerCase()]||a,v[a]=b),this},overrideMimeType:function(a){return null==k&&(o.mimeType=a),this},statusCode:function(a){var b;if(a)if(k)y.always(a[y.status]);else for(b in a)u[b]=[u[b],a[b]];return this},abort:function(a){var b=a||x;return e&&e.abort(b),A(0,b),this}};if(s.promise(y),o.url=((b||o.url||tb.href)+"").replace(Hb,tb.protocol+"//"),o.type=c.method||c.type||o.method||o.type,o.dataTypes=(o.dataType||"*").toLowerCase().match(L)||[""],null==o.crossDomain){j=d.createElement("a");try{j.href=o.url,j.href=j.href,o.crossDomain=Lb.protocol+"//"+Lb.host!=j.protocol+"//"+j.host}catch(z){o.crossDomain=!0}}if(o.data&&o.processData&&"string"!=typeof o.data&&(o.data=r.param(o.data,o.traditional)),Nb(Ib,o,c,y),k)return y;l=r.event&&o.global,l&&0===r.active++&&r.event.trigger("ajaxStart"),o.type=o.type.toUpperCase(),o.hasContent=!Gb.test(o.type),f=o.url.replace(Cb,""),o.hasContent?o.data&&o.processData&&0===(o.contentType||"").indexOf("application/x-www-form-urlencoded")&&(o.data=o.data.replace(Bb,"+")):(n=o.url.slice(f.length),o.data&&(f+=(vb.test(f)?"&":"?")+o.data,delete o.data),o.cache===!1&&(f=f.replace(Db,"$1"),n=(vb.test(f)?"&":"?")+"_="+ub++ +n),o.url=f+n),o.ifModified&&(r.lastModified[f]&&y.setRequestHeader("If-Modified-Since",r.lastModified[f]),r.etag[f]&&y.setRequestHeader("If-None-Match",r.etag[f])),(o.data&&o.hasContent&&o.contentType!==!1||c.contentType)&&y.setRequestHeader("Content-Type",o.contentType),y.setRequestHeader("Accept",o.dataTypes[0]&&o.accepts[o.dataTypes[0]]?o.accepts[o.dataTypes[0]]+("*"!==o.dataTypes[0]?", "+Kb+"; q=0.01":""):o.accepts["*"]);for(m in o.headers)y.setRequestHeader(m,o.headers[m]);if(o.beforeSend&&(o.beforeSend.call(p,y,o)===!1||k))return y.abort();if(x="abort",t.add(o.complete),y.done(o.success),y.fail(o.error),e=Nb(Jb,o,c,y)){if(y.readyState=1,l&&q.trigger("ajaxSend",[y,o]),k)return y;o.async&&o.timeout>0&&(i=a.setTimeout(function(){y.abort("timeout")},o.timeout));try{k=!1,e.send(v,A)}catch(z){if(k)throw z;A(-1,z)}}else A(-1,"No Transport");function A(b,c,d,h){var j,m,n,v,w,x=c;k||(k=!0,i&&a.clearTimeout(i),e=void 0,g=h||"",y.readyState=b>0?4:0,j=b>=200&&b<300||304===b,d&&(v=Pb(o,y,d)),v=Qb(o,v,y,j),j?(o.ifModified&&(w=y.getResponseHeader("Last-Modified"),w&&(r.lastModified[f]=w),w=y.getResponseHeader("etag"),w&&(r.etag[f]=w)),204===b||"HEAD"===o.type?x="nocontent":304===b?x="notmodified":(x=v.state,m=v.data,n=v.error,j=!n)):(n=x,!b&&x||(x="error",b<0&&(b=0))),y.status=b,y.statusText=(c||x)+"",j?s.resolveWith(p,[m,x,y]):s.rejectWith(p,[y,x,n]),y.statusCode(u),u=void 0,l&&q.trigger(j?"ajaxSuccess":"ajaxError",[y,o,j?m:n]),t.fireWith(p,[y,x]),l&&(q.trigger("ajaxComplete",[y,o]),--r.active||r.event.trigger("ajaxStop")))}return y},getJSON:function(a,b,c){return r.get(a,b,c,"json")},getScript:function(a,b){return r.get(a,void 0,b,"script")}}),r.each(["get","post"],function(a,b){r[b]=function(a,c,d,e){return r.isFunction(c)&&(e=e||d,d=c,c=void 0),r.ajax(r.extend({url:a,type:b,dataType:e,data:c,success:d},r.isPlainObject(a)&&a))}}),r._evalUrl=function(a){return r.ajax({url:a,type:"GET",dataType:"script",cache:!0,async:!1,global:!1,"throws":!0})},r.fn.extend({wrapAll:function(a){var b;return this[0]&&(r.isFunction(a)&&(a=a.call(this[0])),b=r(a,this[0].ownerDocument).eq(0).clone(!0),this[0].parentNode&&b.insertBefore(this[0]),b.map(function(){var a=this;while(a.firstElementChild)a=a.firstElementChild;return a}).append(this)),this},wrapInner:function(a){return r.isFunction(a)?this.each(function(b){r(this).wrapInner(a.call(this,b))}):this.each(function(){var b=r(this),c=b.contents();c.length?c.wrapAll(a):b.append(a)})},wrap:function(a){var b=r.isFunction(a);return this.each(function(c){r(this).wrapAll(b?a.call(this,c):a)})},unwrap:function(a){return this.parent(a).not("body").each(function(){r(this).replaceWith(this.childNodes)}),this}}),r.expr.pseudos.hidden=function(a){return!r.expr.pseudos.visible(a)},r.expr.pseudos.visible=function(a){return!!(a.offsetWidth||a.offsetHeight||a.getClientRects().length)},r.ajaxSettings.xhr=function(){try{return new a.XMLHttpRequest}catch(b){}};var Rb={0:200,1223:204},Sb=r.ajaxSettings.xhr();o.cors=!!Sb&&"withCredentials"in Sb,o.ajax=Sb=!!Sb,r.ajaxTransport(function(b){var c,d;if(o.cors||Sb&&!b.crossDomain)return{send:function(e,f){var g,h=b.xhr();if(h.open(b.type,b.url,b.async,b.username,b.password),b.xhrFields)for(g in b.xhrFields)h[g]=b.xhrFields[g];b.mimeType&&h.overrideMimeType&&h.overrideMimeType(b.mimeType),b.crossDomain||e["X-Requested-With"]||(e["X-Requested-With"]="XMLHttpRequest");for(g in e)h.setRequestHeader(g,e[g]);c=function(a){return function(){c&&(c=d=h.onload=h.onerror=h.onabort=h.onreadystatechange=null,"abort"===a?h.abort():"error"===a?"number"!=typeof h.status?f(0,"error"):f(h.status,h.statusText):f(Rb[h.status]||h.status,h.statusText,"text"!==(h.responseType||"text")||"string"!=typeof h.responseText?{binary:h.response}:{text:h.responseText},h.getAllResponseHeaders()))}},h.onload=c(),d=h.onerror=c("error"),void 0!==h.onabort?h.onabort=d:h.onreadystatechange=function(){4===h.readyState&&a.setTimeout(function(){c&&d()})},c=c("abort");try{h.send(b.hasContent&&b.data||null)}catch(i){if(c)throw i}},abort:function(){c&&c()}}}),r.ajaxPrefilter(function(a){a.crossDomain&&(a.contents.script=!1)}),r.ajaxSetup({accepts:{script:"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"},contents:{script:/\b(?:java|ecma)script\b/},converters:{"text script":function(a){return r.globalEval(a),a}}}),r.ajaxPrefilter("script",function(a){void 0===a.cache&&(a.cache=!1),a.crossDomain&&(a.type="GET")}),r.ajaxTransport("script",function(a){if(a.crossDomain){var b,c;return{send:function(e,f){b=r("<script>").prop({charset:a.scriptCharset,src:a.url}).on("load error",c=function(a){b.remove(),c=null,a&&f("error"===a.type?404:200,a.type)}),d.head.appendChild(b[0])},abort:function(){c&&c()}}}});var Tb=[],Ub=/(=)\?(?=&|$)|\?\?/;r.ajaxSetup({jsonp:"callback",jsonpCallback:function(){var a=Tb.pop()||r.expando+"_"+ub++;return this[a]=!0,a}}),r.ajaxPrefilter("json jsonp",function(b,c,d){var e,f,g,h=b.jsonp!==!1&&(Ub.test(b.url)?"url":"string"==typeof b.data&&0===(b.contentType||"").indexOf("application/x-www-form-urlencoded")&&Ub.test(b.data)&&"data");if(h||"jsonp"===b.dataTypes[0])return e=b.jsonpCallback=r.isFunction(b.jsonpCallback)?b.jsonpCallback():b.jsonpCallback,h?b[h]=b[h].replace(Ub,"$1"+e):b.jsonp!==!1&&(b.url+=(vb.test(b.url)?"&":"?")+b.jsonp+"="+e),b.converters["script json"]=function(){return g||r.error(e+" was not called"),g[0]},b.dataTypes[0]="json",f=a[e],a[e]=function(){g=arguments},d.always(function(){void 0===f?r(a).removeProp(e):a[e]=f,b[e]&&(b.jsonpCallback=c.jsonpCallback,Tb.push(e)),g&&r.isFunction(f)&&f(g[0]),g=f=void 0}),"script"}),o.createHTMLDocument=function(){var a=d.implementation.createHTMLDocument("").body;return a.innerHTML="<form></form><form></form>",2===a.childNodes.length}(),r.parseHTML=function(a,b,c){if("string"!=typeof a)return[];"boolean"==typeof b&&(c=b,b=!1);var e,f,g;return b||(o.createHTMLDocument?(b=d.implementation.createHTMLDocument(""),e=b.createElement("base"),e.href=d.location.href,b.head.appendChild(e)):b=d),f=C.exec(a),g=!c&&[],f?[b.createElement(f[1])]:(f=qa([a],b,g),g&&g.length&&r(g).remove(),r.merge([],f.childNodes))},r.fn.load=function(a,b,c){var d,e,f,g=this,h=a.indexOf(" ");return h>-1&&(d=pb(a.slice(h)),a=a.slice(0,h)),r.isFunction(b)?(c=b,b=void 0):b&&"object"==typeof b&&(e="POST"),g.length>0&&r.ajax({url:a,type:e||"GET",dataType:"html",data:b}).done(function(a){f=arguments,g.html(d?r("<div>").append(r.parseHTML(a)).find(d):a)}).always(c&&function(a,b){g.each(function(){c.apply(this,f||[a.responseText,b,a])})}),this},r.each(["ajaxStart","ajaxStop","ajaxComplete","ajaxError","ajaxSuccess","ajaxSend"],function(a,b){r.fn[b]=function(a){return this.on(b,a)}}),r.expr.pseudos.animated=function(a){return r.grep(r.timers,function(b){return a===b.elem}).length},r.offset={setOffset:function(a,b,c){var d,e,f,g,h,i,j,k=r.css(a,"position"),l=r(a),m={};"static"===k&&(a.style.position="relative"),h=l.offset(),f=r.css(a,"top"),i=r.css(a,"left"),j=("absolute"===k||"fixed"===k)&&(f+i).indexOf("auto")>-1,j?(d=l.position(),g=d.top,e=d.left):(g=parseFloat(f)||0,e=parseFloat(i)||0),r.isFunction(b)&&(b=b.call(a,c,r.extend({},h))),null!=b.top&&(m.top=b.top-h.top+g),null!=b.left&&(m.left=b.left-h.left+e),"using"in b?b.using.call(a,m):l.css(m)}},r.fn.extend({offset:function(a){if(arguments.length)return void 0===a?this:this.each(function(b){r.offset.setOffset(this,a,b)});var b,c,d,e,f=this[0];if(f)return f.getClientRects().length?(d=f.getBoundingClientRect(),b=f.ownerDocument,c=b.documentElement,e=b.defaultView,{top:d.top+e.pageYOffset-c.clientTop,left:d.left+e.pageXOffset-c.clientLeft}):{top:0,left:0}},position:function(){if(this[0]){var a,b,c=this[0],d={top:0,left:0};return"fixed"===r.css(c,"position")?b=c.getBoundingClientRect():(a=this.offsetParent(),b=this.offset(),B(a[0],"html")||(d=a.offset()),d={top:d.top+r.css(a[0],"borderTopWidth",!0),left:d.left+r.css(a[0],"borderLeftWidth",!0)}),{top:b.top-d.top-r.css(c,"marginTop",!0),left:b.left-d.left-r.css(c,"marginLeft",!0)}}},offsetParent:function(){return this.map(function(){var a=this.offsetParent;while(a&&"static"===r.css(a,"position"))a=a.offsetParent;return a||ra})}}),r.each({scrollLeft:"pageXOffset",scrollTop:"pageYOffset"},function(a,b){var c="pageYOffset"===b;r.fn[a]=function(d){return T(this,function(a,d,e){var f;return r.isWindow(a)?f=a:9===a.nodeType&&(f=a.defaultView),void 0===e?f?f[b]:a[d]:void(f?f.scrollTo(c?f.pageXOffset:e,c?e:f.pageYOffset):a[d]=e)},a,d,arguments.length)}}),r.each(["top","left"],function(a,b){r.cssHooks[b]=Pa(o.pixelPosition,function(a,c){if(c)return c=Oa(a,b),Ma.test(c)?r(a).position()[b]+"px":c})}),r.each({Height:"height",Width:"width"},function(a,b){r.each({padding:"inner"+a,content:b,"":"outer"+a},function(c,d){r.fn[d]=function(e,f){var g=arguments.length&&(c||"boolean"!=typeof e),h=c||(e===!0||f===!0?"margin":"border");return T(this,function(b,c,e){var f;return r.isWindow(b)?0===d.indexOf("outer")?b["inner"+a]:b.document.documentElement["client"+a]:9===b.nodeType?(f=b.documentElement,Math.max(b.body["scroll"+a],f["scroll"+a],b.body["offset"+a],f["offset"+a],f["client"+a])):void 0===e?r.css(b,c,h):r.style(b,c,e,h)},b,g?e:void 0,g)}})}),r.fn.extend({bind:function(a,b,c){return this.on(a,null,b,c)},unbind:function(a,b){return this.off(a,null,b)},delegate:function(a,b,c,d){return this.on(b,a,c,d)},undelegate:function(a,b,c){return 1===arguments.length?this.off(a,"**"):this.off(b,a||"**",c)}}),r.holdReady=function(a){a?r.readyWait++:r.ready(!0)},r.isArray=Array.isArray,r.parseJSON=JSON.parse,r.nodeName=B,"function"==typeof define&&define.amd&&define("jquery",[],function(){return r});var Vb=a.jQuery,Wb=a.$;return r.noConflict=function(b){return a.$===r&&(a.$=Wb),b&&a.jQuery===r&&(a.jQuery=Vb),r},b||(a.jQuery=a.$=r),r});


// --- SeTeVi-Code ---

    require(["loadApp", "exporter/data"], function (loader, data) {
        loader.loadAppFromJSON(/*GENERATED JSON*/);});var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
define("model/Interfaces/DataNode", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
});
define("model/observe", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var ObActions;
    (function (ObActions) {
        ObActions[ObActions["ChangedName"] = 0] = "ChangedName";
        ObActions[ObActions["RemovedRelationship"] = 1] = "RemovedRelationship";
        ObActions[ObActions["AddedRelationship"] = 2] = "AddedRelationship";
        ObActions[ObActions["ReplacedRelationship"] = 3] = "ReplacedRelationship";
    })(ObActions = exports.ObActions || (exports.ObActions = {}));
    var Observable = (function () {
        function Observable() {
            this.observers = [];
        }
        Observable.prototype.register = function (observer) {
            this.observers.push(observer);
        };
        Observable.prototype.unregister = function (observer) {
            var n = this.observers.indexOf(observer);
            this.observers.splice(n, 1);
        };
        Observable.prototype.notify = function (action, object, position) {
            var i, max;
            for (i = 0, max = this.observers.length; i < max; i += 1) {
                this.observers[i].notify(action, object, position);
            }
        };
        return Observable;
    }());
    exports.Observable = Observable;
});
define("general/Interfaces/IMap", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
});
define("general/NumberMap", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO not used anymore
    var NumberMap = (function () {
        function NumberMap() {
            this.internMap = {};
        }
        NumberMap.prototype.set = function (key, value) {
            this.internMap[key] = value;
        };
        NumberMap.prototype.get = function (key) {
            return this.internMap[key];
        };
        NumberMap.prototype.delete = function (key) {
            this.internMap[key] = null;
        };
        return NumberMap;
    }());
    exports.NumberMap = NumberMap;
});
define("model/IDManager", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var IDManager = (function () {
        function IDManager() {
            this.map = {};
            this.highestID = -1;
        }
        IDManager.prototype.import = function (toImport) {
            var listOfDataNodes = toImport.getAllDataNodes();
            for (var i = 0; i < listOfDataNodes.length; i++) {
                this.importDataNode(listOfDataNodes[i]);
            }
        };
        IDManager.prototype.importDataNode = function (dataNode) {
            dataNode.setDataNodeId(null);
            this.takeDataNode(dataNode);
        };
        IDManager.prototype.getNewId = function () {
            var toReturn = this.highestID;
            this.highestID++;
            return toReturn;
        };
        IDManager.prototype.reset = function () {
            this.map = [];
            this.highestID = -1;
            this.rootNode = null;
        };
        IDManager.prototype.setRootNode = function (rootNode) {
            this.rootNode = rootNode;
        };
        IDManager.prototype.getRootNode = function () {
            return this.rootNode;
        };
        IDManager.prototype.takeDataNode = function (dataNode) {
            if (dataNode.getDataNodeId() == null || dataNode.getDataNodeId() == undefined) {
                this.highestID++;
                dataNode.setDataNodeId(this.highestID);
                this.map[this.highestID] = dataNode;
            }
        };
        IDManager.prototype.removeDataNode = function (dataNode) {
            this.map[dataNode.getDataNodeId()] = null;
        };
        IDManager.prototype.getAllDataNodes = function () {
            var list = [];
            for (var i = 0; i <= this.highestID; i++) {
                var dataNode = this.map[i];
                if (dataNode != null && dataNode != undefined) {
                    list.push(dataNode);
                }
            }
            return list;
        };
        IDManager.prototype.setIdForDataNode = function (dataNode, id) {
            dataNode.setDataNodeId(id);
            this.map[id] = dataNode;
            if (id > this.highestID) {
                this.highestID = id;
            }
        };
        IDManager.prototype.getDataNodeForId = function (id) {
            return this.map[id];
        };
        return IDManager;
    }());
    IDManager.singleton = new IDManager();
    exports.IDManager = IDManager;
});
define("model/HasDetail", ["require", "exports", "model/IDManager"], function (require, exports, IDManager_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var HasDetail = (function () {
        function HasDetail(subject, object) {
            this.subject = subject;
            this.object = object;
        }
        HasDetail.prototype.register = function (observer) {
        };
        HasDetail.prototype.unregister = function (observer) {
        };
        HasDetail.prototype.getDependencies = function () {
            var list = [];
            list.push(this.object, this.subject);
            return list;
        };
        HasDetail.completeStub = function (stub, jsonDataNode, idManager) {
            stub.subject = idManager.getDataNodeForId(jsonDataNode["from"]);
            stub.object = idManager.getDataNodeForId(jsonDataNode["to"]);
        };
        HasDetail.createStubFromJSON = function (jsonDataNode, idManager) {
            var instance = new HasDetail(null, null);
            idManager.setIdForDataNode(instance, jsonDataNode["dataNodeId"]);
            return instance;
        };
        HasDetail.createInstance = function (subject, object) {
            var instance = new HasDetail(subject, object);
            IDManager_1.IDManager.singleton.takeDataNode(instance);
            return instance;
        };
        HasDetail.prototype.delete = function () {
            this.subject = null;
            this.object = null;
            this.onDeleteAttr.call(this);
            IDManager_1.IDManager.singleton.removeDataNode(this);
        };
        HasDetail.prototype.onDelete = function (callback) {
            this.onDeleteAttr = callback;
        };
        HasDetail.prototype.getSubject = function () {
            return this.subject;
        };
        HasDetail.prototype.getObject = function () {
            return this.object;
        };
        HasDetail.prototype.getDataNodeId = function () {
            return this.dataNodeId;
        };
        HasDetail.prototype.getType = function () {
            // not used here
        };
        HasDetail.prototype.getObjectAsJSON = function () {
            var jsonObject = {};
            jsonObject["dataNodeId"] = this.dataNodeId;
            jsonObject["classAttr"] = "HasDetail";
            jsonObject["from"] = this.subject.getDataNodeId();
            jsonObject["to"] = this.object.getDataNodeId();
            return jsonObject;
        };
        HasDetail.prototype.setDataNodeId = function (id) {
            this.dataNodeId = id;
        };
        return HasDetail;
    }());
    exports.HasDetail = HasDetail;
});
define("model/SimpleDataNode", ["require", "exports", "model/observe", "model/HasDetail", "model/IDManager"], function (require, exports, observe_1, HasDetail_1, IDManager_2) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var SimpleDataNode = (function (_super) {
        __extends(SimpleDataNode, _super);
        function SimpleDataNode(name) {
            var _this = _super.call(this) || this;
            _this.relationships = [];
            _this.name = name;
            return _this;
        }
        SimpleDataNode.prototype.getTypInformation = function () {
            throw new Error("Method not implemented.");
        };
        SimpleDataNode.createStubFromJSON = function (jsonDataNode, idManager) {
            var dataNode = new SimpleDataNode(jsonDataNode["name"]);
            idManager.setIdForDataNode(dataNode, jsonDataNode["dataNodeId"]);
            return dataNode;
        };
        SimpleDataNode.completeStub = function (stub, jsonDataNode, idManager) {
            var relationshipsJSON = jsonDataNode["relationships"];
            for (var i = 0; i < relationshipsJSON.length; i++) {
                var currentID = relationshipsJSON[i];
                var currentRelationship = idManager.getDataNodeForId(currentID);
                stub.relationships[i] = currentRelationship;
                stub.configureRelationship(currentRelationship);
            }
        };
        SimpleDataNode.createInstance = function (name) {
            var instance = new SimpleDataNode(name);
            IDManager_2.IDManager.singleton.takeDataNode(instance);
            return instance;
        };
        SimpleDataNode.createHasDetailAndSetConnector = function (from, to) {
            var rel = HasDetail_1.HasDetail.createInstance(from, to);
            from.addRelationship(rel);
        };
        SimpleDataNode.prototype.setDataNodeId = function (id) {
            this.dataNodeId = id;
        };
        SimpleDataNode.prototype.getDataNodeId = function () {
            return this.dataNodeId;
        };
        SimpleDataNode.prototype.configureRelationship = function (relationship) {
            var self = this;
            relationship.onDelete(function () {
                self.deleteRelationship(relationship);
            });
        };
        SimpleDataNode.prototype.getDependencies = function () {
            return this.relationships;
        };
        SimpleDataNode.prototype.deleteRelationship = function (relationship) {
            var index = this.relationships.indexOf(relationship);
            this.relationships.splice(index, 1);
            this.notify(observe_1.ObActions.RemovedRelationship, relationship, index);
        };
        SimpleDataNode.prototype.getObjectAsJSON = function () {
            var jsonObject = {};
            jsonObject["dataNodeId"] = this.dataNodeId;
            jsonObject["name"] = this.name;
            jsonObject["classAttr"] = "SimpleDataNode";
            var jsonRelationshipsList = [];
            for (var i = 0; i < this.relationships.length; i++) {
                jsonRelationshipsList[i] = this.relationships[i].getDataNodeId();
            }
            jsonObject["relationships"] = jsonRelationshipsList;
            return jsonObject;
        };
        SimpleDataNode.prototype.getName = function () {
            return this.name;
        };
        SimpleDataNode.prototype.setName = function (name) {
            console.log("setName (datenebene)");
            this.name = name;
            this.notify(observe_1.ObActions.ChangedName, null, null);
        };
        SimpleDataNode.prototype.addRelationshipAtPosition = function (toAdd, position) {
            this.relationships.splice(position, 0, toAdd);
            this.configureRelationship(toAdd);
            this.notify(observe_1.ObActions.AddedRelationship, toAdd, position);
        };
        SimpleDataNode.prototype.replaceRelationshipAtPosition = function (newRelationship, position) {
            this.relationships.splice(position, 1, newRelationship);
            this.configureRelationship(newRelationship);
            this.notify(observe_1.ObActions.ReplacedRelationship, newRelationship, position);
        };
        SimpleDataNode.prototype.addRelationship = function (relationship) {
            this.relationships.push(relationship);
            this.configureRelationship(relationship);
            this.notify(observe_1.ObActions.AddedRelationship, relationship, this.relationships.length - 1);
        };
        SimpleDataNode.prototype.getRelationships = function () {
            return this.relationships;
        };
        SimpleDataNode.prototype.getType = function () {
            // not used here
        };
        return SimpleDataNode;
    }(observe_1.Observable));
    exports.SimpleDataNode = SimpleDataNode;
});
define("model/DataTypes", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var DataTypes;
    (function (DataTypes) {
        DataTypes[DataTypes["NamedLinkType"] = 0] = "NamedLinkType";
    })(DataTypes = exports.DataTypes || (exports.DataTypes = {}));
});
define("model/TextObject", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO: not used at the moment
    var TextObject = (function () {
        function TextObject(text) {
            this._linksTo = null;
            this._text = text;
        }
        Object.defineProperty(TextObject.prototype, "isLink", {
            get: function () {
                return this._isLink;
            },
            set: function (value) {
                this._isLink = value;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(TextObject.prototype, "text", {
            get: function () {
                return this._text;
            },
            set: function (value) {
                this._text = value;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(TextObject.prototype, "linksTo", {
            get: function () {
                return this._linksTo;
            },
            set: function (value) {
                this._linksTo = value;
            },
            enumerable: true,
            configurable: true
        });
        return TextObject;
    }());
    exports.TextObject = TextObject;
});
define("model/InverseNamedLink", ["require", "exports", "model/DataTypes", "model/observe", "model/IDManager"], function (require, exports, DataTypes_1, observe_2, IDManager_3) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var InverseNamedLink = (function (_super) {
        __extends(InverseNamedLink, _super);
        function InverseNamedLink(concreteNamedLink) {
            var _this = _super.call(this) || this;
            _this.hasOwnName = false;
            _this.originalNamedLink = concreteNamedLink;
            return _this;
        }
        InverseNamedLink.prototype.getDependencies = function () {
            // TODO
            var list = [];
            return list;
        };
        InverseNamedLink.prototype.originalNamedLinkHasBeenDeleted = function () {
            this.nameOfThisInverseNamedLink = "*this link has been deleted*";
            this.onDeleteAttr.call(this);
            IDManager_3.IDManager.singleton.removeDataNode(this);
        };
        InverseNamedLink.prototype.deleteRelationship = function () {
            this.originalNamedLink.deleteRelationship();
        };
        InverseNamedLink.prototype.onDelete = function (callback) {
            this.onDeleteAttr = callback;
        };
        InverseNamedLink.prototype.getName = function () {
            if (this.hasOwnName) {
                return this.nameOfThisInverseNamedLink;
            }
            else {
                var inverseName = void 0;
                inverseName = this.originalNamedLink.getName() + "-inverse";
                return inverseName;
            }
        };
        InverseNamedLink.prototype.getTo = function () {
            return this.originalNamedLink.getFrom();
        };
        InverseNamedLink.prototype.setName = function (name) {
            this.nameOfThisInverseNamedLink = name;
            this.hasOwnName = true;
            this.notify(observe_2.ObActions.ChangedName, null, null);
        };
        InverseNamedLink.prototype.getObjectAsJSON = function () {
            var jsonObject = {};
            jsonObject["dataNodeId"] = this.dataNodeId;
            jsonObject["classAttr"] = "InverseNamedLink";
            jsonObject["originalNamedLink"] = this.originalNamedLink.getDataNodeId();
            return jsonObject;
        };
        InverseNamedLink.completeStub = function (stub, jsonDataNode, idManager) {
            stub.originalNamedLink = idManager.getDataNodeForId(jsonDataNode["originalNamedLink"]);
        };
        InverseNamedLink.createStubFromJSON = function (jsonDataNode, idManager) {
            var instance = new InverseNamedLink(null);
            idManager.setIdForDataNode(instance, jsonDataNode["dataNodeId"]);
            return instance;
        };
        InverseNamedLink.createInstance = function (concreteNamedLink) {
            var instance = new InverseNamedLink(concreteNamedLink);
            IDManager_3.IDManager.singleton.takeDataNode(instance);
            return instance;
        };
        InverseNamedLink.prototype.getDataNodeId = function () {
            return this.dataNodeId;
        };
        InverseNamedLink.prototype.setDataNodeId = function (id) {
            this.dataNodeId = id;
        };
        InverseNamedLink.prototype.getType = function () {
            return DataTypes_1.DataTypes.NamedLinkType;
        };
        InverseNamedLink.prototype.nameOfOriginalNamedLinkChanged = function () {
            if (this.hasOwnName) {
                // do nothing ...
            }
            else {
                this.notify(observe_2.ObActions.ChangedName, null, null);
            }
        };
        return InverseNamedLink;
    }(observe_2.Observable));
    exports.InverseNamedLink = InverseNamedLink;
});
define("model/NamedLink", ["require", "exports", "model/observe", "model/InverseNamedLink", "model/DataTypes", "model/IDManager"], function (require, exports, observe_3, InverseNamedLink_1, DataTypes_2, IDManager_4) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var OriginalNamedLink = (function (_super) {
        __extends(OriginalNamedLink, _super);
        function OriginalNamedLink() {
            return _super.call(this) || this;
        }
        OriginalNamedLink.prototype.getDependencies = function () {
            var list = [];
            list.push(this.from, this.to, this.inverseNamedLink);
            return list;
        };
        OriginalNamedLink.createInstance = function (name, from, to) {
            var instance = new OriginalNamedLink();
            instance.name = name;
            instance.inverseNamedLink = InverseNamedLink_1.InverseNamedLink.createInstance(instance);
            instance.setFrom(from);
            instance.setTo(to);
            IDManager_4.IDManager.singleton.takeDataNode(instance);
            return instance;
        };
        OriginalNamedLink.completeStub = function (stub, jsonDataNode, idManager) {
            stub.name = jsonDataNode["name"];
            stub.inverseNamedLink = idManager.getDataNodeForId(jsonDataNode["inverseNamedLink"]);
            stub.from = idManager.getDataNodeForId(jsonDataNode["from"]);
            stub.to = idManager.getDataNodeForId(jsonDataNode["to"]);
        };
        OriginalNamedLink.createStubFromJSON = function (jsonDataNode, idManager) {
            var instance = new OriginalNamedLink();
            idManager.setIdForDataNode(instance, jsonDataNode["dataNodeId"]);
            return instance;
        };
        OriginalNamedLink.prototype.deleteRelationship = function () {
            console.log("deleteRelationship auf OriginalNamedLink");
            this.from = null;
            this.to = null;
            this.name = null;
            this.onDeleteAttr.call(this);
            this.inverseNamedLink.originalNamedLinkHasBeenDeleted();
            IDManager_4.IDManager.singleton.removeDataNode(this);
        };
        OriginalNamedLink.prototype.onDelete = function (callback) {
            this.onDeleteAttr = callback;
        };
        OriginalNamedLink.prototype.getInverseNamedLink = function () {
            return this.inverseNamedLink;
        };
        OriginalNamedLink.prototype.getType = function () {
            return DataTypes_2.DataTypes.NamedLinkType;
        };
        OriginalNamedLink.prototype.getObjectAsJSON = function () {
            var jsonObject = {};
            jsonObject["dataNodeId"] = this.dataNodeId;
            jsonObject["name"] = this.name;
            jsonObject["classAttr"] = "OriginalNamedLink";
            jsonObject["inverseNamedLink"] = this.inverseNamedLink.getDataNodeId();
            jsonObject["to"] = this.to.getDataNodeId();
            jsonObject["from"] = this.from.getDataNodeId();
            return jsonObject;
        };
        OriginalNamedLink.prototype.getName = function () {
            return this.name;
        };
        OriginalNamedLink.prototype.setName = function (name) {
            this.name = name;
            this.notify(observe_3.ObActions.ChangedName, null, null);
            this.inverseNamedLink.nameOfOriginalNamedLinkChanged();
        };
        OriginalNamedLink.prototype.getTo = function () {
            return this.to;
        };
        OriginalNamedLink.prototype.setFrom = function (from) {
            // TODO eigentlich müsste zuvor der alte "Connector" geloescht werden
            this.from = from;
            // this.notify("setFrom", from, -1);
        };
        OriginalNamedLink.prototype.setTo = function (to) {
            // TODO eigentlich müsste zuvor der alte "Connector" geloescht werden
            this.to = to;
            // this.notify("setTo", to, -1);
        };
        OriginalNamedLink.prototype.getFrom = function () {
            return this.from;
        };
        OriginalNamedLink.prototype.getDataNodeId = function () {
            return this.dataNodeId;
        };
        OriginalNamedLink.prototype.setDataNodeId = function (id) {
            this.dataNodeId = id;
        };
        return OriginalNamedLink;
    }(observe_3.Observable));
    exports.OriginalNamedLink = OriginalNamedLink;
});
define("model/PlaceholderRelationship", ["require", "exports", "model/IDManager"], function (require, exports, IDManager_5) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var PlaceholderRelationship = (function () {
        function PlaceholderRelationship() {
        }
        PlaceholderRelationship.prototype.onDelete = function (callback) {
            this.onDeleteAttr = callback;
        };
        PlaceholderRelationship.prototype.getDependencies = function () {
            var list = [];
            return list;
        };
        PlaceholderRelationship.prototype.register = function (observer) {
        };
        PlaceholderRelationship.createInstance = function () {
            var instance = new PlaceholderRelationship();
            IDManager_5.IDManager.singleton.takeDataNode(instance);
            return instance;
        };
        PlaceholderRelationship.completeStub = function (stub, jsonDataNode, idManager) {
        };
        PlaceholderRelationship.createStubFromJSON = function (jsonDataNode, idManager) {
            var instance = new PlaceholderRelationship();
            idManager.setIdForDataNode(instance, jsonDataNode["dataNodeId"]);
            return instance;
        };
        PlaceholderRelationship.prototype.delete = function () {
            this.onDeleteAttr.call(this);
            IDManager_5.IDManager.singleton.removeDataNode(this);
        };
        PlaceholderRelationship.prototype.unregister = function (observer) {
        };
        PlaceholderRelationship.prototype.getDataNodeId = function () {
            return this.dataNodeId;
        };
        PlaceholderRelationship.prototype.setDataNodeId = function (id) {
            this.dataNodeId = id;
        };
        PlaceholderRelationship.prototype.getType = function () {
        };
        PlaceholderRelationship.prototype.getObjectAsJSON = function () {
            var jsonObject = {};
            jsonObject["dataNodeId"] = this.dataNodeId;
            jsonObject["classAttr"] = "PlaceholderRelationship";
            return jsonObject;
        };
        PlaceholderRelationship.prototype.getName = function () {
            console.log("getName() not implemented");
        };
        return PlaceholderRelationship;
    }());
    exports.PlaceholderRelationship = PlaceholderRelationship;
});
define("general/Set", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var Set = (function () {
        function Set() {
            this.list = [];
        }
        Set.prototype.has = function (object) {
            for (var i = 0; i < this.list.length; i++) {
                if (this.list[i] === object) {
                    return true;
                }
            }
            return false;
        };
        Set.prototype.push = function (object) {
            this.list.push(object);
        };
        return Set;
    }());
    exports.Set = Set;
});
define("model/ExportImport", ["require", "exports", "model/SimpleDataNode", "model/IDManager", "model/HasDetail", "model/NamedLink", "model/InverseNamedLink", "model/PlaceholderRelationship", "general/Set"], function (require, exports, SimpleDataNode_1, IDManager_6, HasDetail_2, NamedLink_1, InverseNamedLink_2, PlaceholderRelationship_1, Set_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    function getJSONObjectWithAllDataNodes() {
        var listOfAllDataNodes = IDManager_6.IDManager.singleton.getAllDataNodes();
        return listOfDataNodes_To_JSON(listOfAllDataNodes);
    }
    exports.getJSONObjectWithAllDataNodes = getJSONObjectWithAllDataNodes;
    function listOfDataNodes_To_JSON(dataNodes) {
        var list = [];
        for (var i = 0; i < dataNodes.length; i++) {
            list.push(dataNodes[i].getObjectAsJSON());
        }
        return list;
    }
    function getExportAsJson_Object(dataNode) {
        var dependencies = getAllDependencies(dataNode);
        var jsonObject = {};
        jsonObject["rootNode"] = dataNode.getDataNodeId();
        jsonObject["listOfAllDataNodes"] = listOfDataNodes_To_JSON(dependencies);
        return jsonObject;
    }
    exports.getExportAsJson_Object = getExportAsJson_Object;
    function getAllDependencies(dataNode) {
        visited = new Set_1.Set();
        todos = [];
        dependencies = [];
        todos.push(dataNode);
        workTodoList();
        return dependencies;
    }
    function workTodoList() {
        var currentDataNode;
        while (todos.length > 0) {
            currentDataNode = todos.pop();
            if (!visited.has(currentDataNode)) {
                visit(currentDataNode);
            }
        }
    }
    function visit(dataNode) {
        visited.push(dataNode);
        dependencies.push(dataNode);
        var dependenciesOfDataNode = dataNode.getDependencies();
        for (var i = 0; i < dependenciesOfDataNode.length; i++) {
            var currentDependency = dependenciesOfDataNode[i];
            todos.push(currentDependency);
        }
    }
    function getExportAsJson() {
        var jsonObject = {};
        jsonObject["rootNode"] = IDManager_6.IDManager.singleton.getRootNode().getDataNodeId();
        jsonObject["listOfAllDataNodes"] = getJSONObjectWithAllDataNodes();
        return jsonObject;
    }
    exports.getExportAsJson = getExportAsJson;
    function createDataNodeStub(jsonDataNode, idManager) {
        var classAttr = jsonDataNode["classAttr"];
        if (classAttr == "SimpleDataNode") {
            return SimpleDataNode_1.SimpleDataNode.createStubFromJSON(jsonDataNode, idManager);
        }
        else if (classAttr == "HasDetail") {
            return HasDetail_2.HasDetail.createStubFromJSON(jsonDataNode, idManager);
        }
        else if (classAttr == "OriginalNamedLink") {
            return NamedLink_1.OriginalNamedLink.createStubFromJSON(jsonDataNode, idManager);
        }
        else if (classAttr == "InverseNamedLink") {
            return InverseNamedLink_2.InverseNamedLink.createStubFromJSON(jsonDataNode, idManager);
        }
        else if (classAttr == "PlaceholderRelationship") {
            return PlaceholderRelationship_1.PlaceholderRelationship.createStubFromJSON(jsonDataNode, idManager);
        }
        else {
            console.log("could not create DataNodeStub");
        }
    }
    exports.createDataNodeStub = createDataNodeStub;
    function completeStub(jsonDataNode, idManager) {
        var stub = idManager.getDataNodeForId(jsonDataNode["dataNodeId"]);
        var classAttr = jsonDataNode["classAttr"];
        if (classAttr == "SimpleDataNode") {
            return SimpleDataNode_1.SimpleDataNode.completeStub(stub, jsonDataNode, idManager);
        }
        else if (classAttr == "HasDetail") {
            return HasDetail_2.HasDetail.completeStub(stub, jsonDataNode, idManager);
        }
        else if (classAttr == "OriginalNamedLink") {
            return NamedLink_1.OriginalNamedLink.completeStub(stub, jsonDataNode, idManager);
        }
        else if (classAttr == "InverseNamedLink") {
            return InverseNamedLink_2.InverseNamedLink.completeStub(stub, jsonDataNode, idManager);
        }
        else if (classAttr == "PlaceholderRelationship") {
            return PlaceholderRelationship_1.PlaceholderRelationship.completeStub(stub, jsonDataNode, idManager);
        }
        else {
            console.log("could not complete stub");
        }
    }
    exports.completeStub = completeStub;
    function getDataNodes(jsonObject, idManager) {
        idManager.reset();
        var rootNode = jsonObject["rootNode"];
        var listOfAllDataNodes_JSON = jsonObject["listOfAllDataNodes"];
        for (var i = 0; i < listOfAllDataNodes_JSON.length; i++) {
            createDataNodeStub(listOfAllDataNodes_JSON[i], idManager);
        }
        for (var i = 0; i < listOfAllDataNodes_JSON.length; i++) {
            completeStub(listOfAllDataNodes_JSON[i], idManager);
        }
        idManager.setRootNode(idManager.getDataNodeForId(rootNode));
    }
    exports.getDataNodes = getDataNodes;
    var visited;
    var todos;
    var dependencies;
});
define("visual/ColorManagement", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    function getColorForChild(color) {
        return (color + 1) % 2;
    }
    exports.getColorForChild = getColorForChild;
    function getColorValue(color) {
        switch (color) {
            case Colors.Beige:
                return "beige";
            case Colors.White:
                return "white";
            case Colors.LightGrey:
                return "lightgrey";
            case Colors.LightBlue:
                return "lightblue";
            case Colors.LightGreen:
                return "lightgreen";
            case Colors.Black:
                return "black";
            case Colors.Grey:
                return "grey";
            case Colors.DarkGrey:
                return "#3A3A3A";
            case Colors.LightBlueCool:
                return "#D9F2FF";
            case Colors.LightBlueGreen:
                return "#C1FFE8";
            case Colors.LightLightBlue:
                return "#EDFCFB";
            case Colors.LightLightOrange:
                return "#FFF8EF";
            case Colors.LightLightGreen:
                return "#F4FFF0";
            case Colors.LightLightGrey:
                return "#EAEAEA";
            case Colors.LightLightLightLightGrey:
                return "#f5f5f5";
            case Colors.LightLightLightGrey:
                return "#efefef";
        }
    }
    exports.getColorValue = getColorValue;
    var Colors;
    (function (Colors) {
        Colors[Colors["LightLightLightGrey"] = 0] = "LightLightLightGrey";
        Colors[Colors["White"] = 1] = "White";
        Colors[Colors["LightLightGrey"] = 2] = "LightLightGrey";
        Colors[Colors["LightLightLightLightGrey"] = 3] = "LightLightLightLightGrey";
        Colors[Colors["LightGrey"] = 4] = "LightGrey";
        Colors[Colors["Beige"] = 5] = "Beige";
        Colors[Colors["LightLightOrange"] = 6] = "LightLightOrange";
        Colors[Colors["LightBlueCool"] = 7] = "LightBlueCool";
        Colors[Colors["LightLightBlue"] = 8] = "LightLightBlue";
        Colors[Colors["LightLightGreen"] = 9] = "LightLightGreen";
        Colors[Colors["LightBlueGreen"] = 10] = "LightBlueGreen";
        Colors[Colors["LightBlue"] = 11] = "LightBlue";
        Colors[Colors["LightGreen"] = 12] = "LightGreen";
        Colors[Colors["Black"] = 13] = "Black";
        Colors[Colors["Grey"] = 14] = "Grey";
        Colors[Colors["DarkGrey"] = 15] = "DarkGrey";
    })(Colors = exports.Colors || (exports.Colors = {}));
});
define("visual/Callbacks", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO
    var Callbacks = (function () {
        function Callbacks() {
        }
        Callbacks.prototype.leavesWithEnter = function () {
            this.onLeavesWithEnterAttr.call(this);
        };
        Callbacks.prototype.emitsCursorTop = function () {
            this.onEmitsCursorTopAttr.call(this);
        };
        Callbacks.prototype.emitsCursorBottom = function () {
            this.onEmitsCursorBottomAttr.call(this);
        };
        Callbacks.prototype.delete = function () {
            this.onDeleteAttr.call(this);
        };
        Callbacks.prototype.onLeavesWithEnter = function (callback) {
            this.onLeavesWithEnterAttr = callback;
        };
        Callbacks.prototype.onDelete = function (callback) {
            this.onDeleteAttr = callback;
        };
        Callbacks.prototype.onEmitsCursorTop = function (callback) {
            this.onEmitsCursorTopAttr = callback;
        };
        Callbacks.prototype.onEmitsCursorBottom = function (callback) {
            this.onEmitsCursorBottomAttr = callback;
        };
        return Callbacks;
    }());
    exports.Callbacks = Callbacks;
});
define("visual/Interfaces/interfaces", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
});
define("visual/general", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    function getVisualNodeWithFocus() {
        var nativeFocused = document.activeElement;
        return nativeFocused.visualNode; // TODO get type
    }
    exports.getVisualNodeWithFocus = getVisualNodeWithFocus;
    exports.STANDARD_HORIZONTAL_MARGIN = 3;
    exports.INDENTATION_PADDING = 6;
    exports.STANDARD_VERTICAL_MARGIN = 3;
    exports.STANDARD_PADDING = 3;
    exports.STANDARD_MARGIN = 3;
    exports.EDGE_RADIUS = "3px";
    exports.NODE_DISPLAY = "inline-block";
    exports.FONT = "sans-serif";
    exports.FONT_SIZE = "12pt";
    exports.MAX_WIDTH_OF_NODE_VIEW = 800;
    exports.BOX_SHADOW_NODE = "2px 2px 1px #999";
    // export const BOX_SHADOW_NODE : string = "1px 1px 1px 1px #999";
    exports.MAXIMUM_WIDTH_OF_NODE = 600;
    // TODO delete
    exports.PADING_NODE = 3;
    exports.DISTANCE_BETWEEN_HEAD_AND_CHILDREN = 3;
    exports.MARGIN_RIGHT_BODY = 8;
    exports.MARGIN_LEFT_BODY = 8;
    exports.DISTANCE_BETWEEN_NODES = "4px";
    exports.INDENTATION = 8;
    exports.focusedObject = null;
    function getFocusedObject() {
        return exports.focusedObject;
    }
    exports.getFocusedObject = getFocusedObject;
    function setFocusedObject(newFocusedObject) {
        exports.focusedObject = newFocusedObject;
    }
    exports.setFocusedObject = setFocusedObject;
});
define("visual/TextField", ["require", "exports", "visual/Callbacks", "visual/ColorManagement", "visual/general"], function (require, exports, Callbacks_1, ColorManagement_1, general_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var TextField = (function () {
        function TextField(text, eventAcceptor) {
            this.callbacks = new Callbacks_1.Callbacks();
            this._mySpan = this.createUIObject(text, eventAcceptor);
        }
        TextField.prototype.getCallbacks = function () {
            return this.callbacks;
        };
        TextField.prototype.onTextChange = function (callback) {
            this.onTextChangeAttr = callback;
        };
        TextField.prototype.setFontColor = function (fontColor) {
            this.fontColor = fontColor;
            this._mySpan.style.color = ColorManagement_1.getColorValue(this.fontColor);
        };
        TextField.prototype.setBackgroundColor = function (color) {
            this.backgroundColor = color;
            this._mySpan.style.backgroundColor = ColorManagement_1.getColorValue(this.fontColor);
        };
        TextField.prototype.takeCursor = function () {
            var range;
            var selection;
            var element = this._mySpan;
            range = document.createRange();
            range.selectNodeContents(element);
            range.collapse(true);
            selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            element.focus(); // the cursor is visible only if the element is focused
        };
        TextField.prototype.setText = function (newText) {
            this._mySpan.innerText = newText;
        };
        TextField.prototype.getText = function () {
            return this._mySpan.innerText;
        };
        TextField.prototype.createUIObject = function (text, eventAcceptor) {
            var UIObject = document.createElement("span");
            UIObject.innerHTML = text;
            UIObject.style.wordWrap = "break-word";
            UIObject.style.textDecoration = "inherit";

            UIObject.style.font = general_1.FONT_SIZE + " " + general_1.FONT;
            UIObject.contentEditable = "false";
            UIObject.userEventAcceptor = eventAcceptor;
            var self = this;
            UIObject.oninput = function () {
                self.textChanged();
            };
            return UIObject;
        };
        TextField.prototype.getUIObject = function () {
            return this._mySpan;
        };
        TextField.prototype.textChanged = function () {
            this.onTextChangeAttr.call(this);
        };
        return TextField;
    }());
    exports.TextField = TextField;
});
define("visual/FocusableTextField", ["require", "exports", "visual/TextField"], function (require, exports, TextField_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var FocusableTextField = (function (_super) {
        __extends(FocusableTextField, _super);
        function FocusableTextField(text, backgroundColor, eventAcceptor) {
            var _this = _super.call(this, text, eventAcceptor) || this;
            _this.setBackgroundColor(backgroundColor);
            return _this;
        }
        FocusableTextField.prototype.takeCursorFromBottom = function () {
            this.takeCursor();
        };
        FocusableTextField.prototype.takeCursorFromTop = function () {
            this.takeCursor();
        };
        FocusableTextField.prototype.focus = function () {
            this.takeCursor();
        };
        // not used here:
        FocusableTextField.prototype.getDataNode = function () {
            return undefined;
        };
        FocusableTextField.prototype.zoomInPossible = function () {
            return undefined;
        };
        FocusableTextField.prototype.zoomOutPossible = function () {
            return undefined;
        };
        FocusableTextField.prototype.zoomIn = function () {
        };
        FocusableTextField.prototype.zoomOut = function () {
        };
        FocusableTextField.prototype.removeFocus = function () {
        };
        return FocusableTextField;
    }(TextField_1.TextField));
    exports.FocusableTextField = FocusableTextField;
});
define("general/List", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var List = (function () {
        function List() {
            this.objects = [];
        }
        // It is allowed that position == length. (that means toInsert is appended to the list)
        List.prototype.insert = function (toInsert, position) {
            if (position < this.objects.length) {
                this.objects.splice(position, 0, toInsert);
            }
            else if (position == this.objects.length) {
                this.objects[position] = toInsert;
            }
        };
        List.prototype.remove = function (position) {
            this.objects.splice(position, 1);
        };
        List.prototype.get = function (position) {
            return this.objects[position];
        };
        List.prototype.getIndex = function (object) {
            for (var i = 0; i < this.objects.length; i++) {
                if (this.objects[i] == object) {
                    return i;
                }
            }
            return -1;
        };
        List.prototype.getNext = function (object) {
            var index = this.getIndex(object);
            if (index + 1 < this.objects.length) {
                return this.objects[index + 1];
            }
            else {
                return null;
            }
        };
        List.prototype.getPrevious = function (object) {
            var index = this.getIndex(object);
            if (index > 0) {
                return this.objects[index - 1];
            }
            else {
                return null;
            }
        };
        List.prototype.getLength = function () {
            return this.objects.length;
        };
        return List;
    }());
    exports.List = List;
});
define("visual/ListController", ["require", "exports", "visual/Callbacks", "general/List"], function (require, exports, Callbacks_2, List_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var ListController = (function (_super) {
        __extends(ListController, _super);
        function ListController(listElements, maxWidth) {
            var _this = _super.call(this) || this;
            _this.subVisualNodes = new List_1.List();
            _this.callbacks = new Callbacks_2.Callbacks();
            _this.myDiv = document.createElement('div');
            _this.myDiv.style.width = _this.maxWidth + "px";
            _this.setMaxWidth(maxWidth);
            for (var i = 0; i < listElements.length; i++) {
                _this.insertVisualNodeAtPosition(listElements[i], i);
            }
            return _this;
        }
        ListController.prototype.getCallbacks = function () {
            return this.callbacks;
        };
        ListController.prototype.setParentZoomOutHandler = function (parentZoomOutHandler) {
        };
        ListController.prototype.configureListElement = function (listElem) {
            var self = this;
            listElem.setMaxWidth(this.maxWidthForChildren);
            listElem.getCallbacks().onEmitsCursorTop(function () {
                self.childEmitsCursorTop(listElem);
            });
            listElem.getCallbacks().onEmitsCursorBottom(function () {
                self.childEmitsCursorBottom(listElem);
            });
            listElem.getCallbacks().onLeavesWithEnter(function () {
                self.childLeavesWithEnter(listElem);
            });
        };
        ListController.prototype.childEmitsCursorTop = function (child) {
            var previousChild = this.subVisualNodes.getPrevious(child);
            if (previousChild == null) {
                this.emitsCursorTop();
            }
            else {
                previousChild.takeCursorFromBottom();
            }
        };
        ListController.prototype.childEmitsCursorBottom = function (child) {
            var nextChild = this.subVisualNodes.getNext(child);
            if (nextChild == null) {
                this.emitsCursorBottom();
            }
            else {
                nextChild.takeCursorFromTop();
            }
        };
        ListController.prototype.childLeavesWithEnter = function (visualNode) {
            this.onChildLeavesWithEnterAttr.call(this, visualNode);
        };
        ListController.prototype.onChildLeavesWithEnter = function (callback) {
            this.onChildLeavesWithEnterAttr = callback;
        };
        ListController.prototype.zoomIn = function () {
            for (var i = 0; i < this.subVisualNodes.getLength(); i++) {
                this.subVisualNodes.get(i).zoomIn();
            }
        };
        ListController.prototype.zoomOut = function () {
            for (var i = 0; i < this.subVisualNodes.getLength(); i++) {
                this.subVisualNodes.get(i).zoomOut();
            }
        };
        ListController.prototype.zoomInPossible = function () {
            return undefined;
        };
        ListController.prototype.zoomOutPossible = function () {
            for (var i = 0; i < this.subVisualNodes.getLength(); i++) {
                if (this.subVisualNodes.get(i).zoomOutPossible()) {
                    return true;
                }
            }
            return false;
        };
        ListController.prototype.getVisualNodeAtPosition = function (position) {
            return this.subVisualNodes.get(position);
        };
        ListController.prototype.insertVisualNodeAtPosition = function (visualNode, position) {
            this.configureListElement(visualNode);
            var visualNodeDiv = visualNode.getUIObject();
            if (position == this.subVisualNodes.getLength()) {
                this.myDiv.appendChild(visualNodeDiv);
            }
            else {
                // it is possible that myDiv.children.length > subVisualNodes.getLength()
                var UIObject_After = this.subVisualNodes.get(position).getUIObject();
                this.myDiv.insertBefore(visualNodeDiv, UIObject_After);
            }
            this.subVisualNodes.insert(visualNode, position);
        };
        ListController.prototype.removeVisualNodeAtPosition = function (position) {
            this.subVisualNodes.get(position).removeFromDOM();
            this.subVisualNodes.remove(position);
        };
        ListController.prototype.focusVisualNodeAtPosition = function (position) {
            this.subVisualNodes.get(position).takeCursorFromTop();
        };
        ListController.prototype.getUIObject = function () {
            return this.myDiv;
        };
        ListController.prototype.setMaxWidth = function (maxWidth) {
            this.maxWidth = maxWidth;
            this.set_maxWidthForChildren();
            for (var i = 0; i < this.subVisualNodes.getLength(); i++) {
                this.subVisualNodes.get(i).setMaxWidth(this.maxWidthForChildren);
            }
        };
        ListController.prototype.set_maxWidthForChildren = function () {
            // this.maxWidthForChildren = this.maxWidth - INDENTATION - INDENTATION - 3;
            this.maxWidthForChildren = this.maxWidth;
        };
        ListController.prototype.getIndexOfChild = function (child) {
            return this.subVisualNodes.getIndex(child);
        };
        ListController.prototype.takeCursorFromBottom = function () {
            var lastChildren = this.subVisualNodes.get(this.subVisualNodes.getLength() - 1);
            lastChildren.takeCursorFromBottom();
        };
        ListController.prototype.takeCursorFromTop = function () {
            this.subVisualNodes.get(0).takeCursorFromTop();
        };
        ListController.prototype.getDataNode = function () {
            // not used here ...
            return undefined;
        };
        ListController.prototype.focus = function () {
        };
        ListController.prototype.removeFocus = function () {
        };
        return ListController;
    }(Callbacks_2.Callbacks));
    exports.ListController = ListController;
});
define("visual/Clipboard", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var Clipboard = (function () {
        function Clipboard() {
        }
        Clipboard.prototype.putIntoClipboard = function (dataNode) {
            this.storedDataNode = dataNode;
            console.log("put into clipboard: " + JSON.stringify(this.storedDataNode.getObjectAsJSON()));
        };
        Clipboard.prototype.getDataNode = function () {
            return this.storedDataNode;
        };
        return Clipboard;
    }());
    Clipboard.singleton = new Clipboard();
    exports.Clipboard = Clipboard;
});
define("visual/Utils", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var Utils = (function () {
        function Utils() {
        }
        Utils.remove = function (toRemove) {
            toRemove.parentNode.removeChild(toRemove);
        };
        Utils.insertAfter = function (htmlObject, toInsert) {
            var parent = htmlObject.parentNode;
            var next = htmlObject.nextSibling;
            if (next == null) {
                parent.appendChild(toInsert);
            }
            else {
                parent.insertBefore(toInsert, next);
            }
        };
        Utils.removeNext = function (htmlObject) {
            Utils.remove(htmlObject.nextSibling);
        };
        Utils.getDiv = function () {
            return document.createElement('div');
        };
        return Utils;
    }());
    exports.Utils = Utils;
});
define("visual/BodyContainer", ["require", "exports", "visual/ColorManagement", "visual/general", "visual/Utils"], function (require, exports, ColorManagement_2, general_2, Utils_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var BodyContainer = (function () {
        function BodyContainer(backgroundColor) {
            this.myDiv = Utils_1.Utils.getDiv();
            this.containerDiv = null;
            this.backgroundColor = backgroundColor;
            this.createUIObject();
        }
        BodyContainer.prototype.setMaxWidth = function (maxWidth) {
            this.maxWidth = maxWidth;
            this.containerDiv.style.width = this.maxWidth + "px";
            this.content.setMaxWidth(this.maxWidth - 2 * (general_2.INDENTATION_PADDING + general_2.STANDARD_MARGIN));
        };
        BodyContainer.prototype.createUIObject = function () {
            var width = this.maxWidth;
            this.containerDiv = Utils_1.Utils.getDiv();
            this.containerDiv.style.marginLeft = general_2.STANDARD_MARGIN + "px";
            this.containerDiv.style.marginRight = general_2.STANDARD_MARGIN + "px";
            this.containerDiv.style.marginBottom = general_2.STANDARD_MARGIN + "px";
            this.containerDiv.style.padding = general_2.STANDARD_PADDING + "px";
            this.containerDiv.style.paddingLeft = general_2.INDENTATION_PADDING + "px";
            this.containerDiv.style.paddingRight = general_2.INDENTATION_PADDING + "px";
            this.containerDiv.style.overflow = "hidden";
            this.containerDiv.style.backgroundColor = ColorManagement_2.getColorValue(this.backgroundColor);
            this.containerDiv.style.display = "inline-block"; // otherwise the shadow of head looks ugly
            this.containerDiv.style.width = this.maxWidth + "px";
            this.containerDiv.style.boxShadow = general_2.BOX_SHADOW_NODE;
            var fontSizeDiv = Utils_1.Utils.getDiv();
            fontSizeDiv.appendChild(this.containerDiv);
            fontSizeDiv.style.fontSize = "0%"; // to prevent gap (at the beginning of the animation) caused by inline-block of containerDiv
            this.containerDiv.style.fontSize = "12pt"; // normalize fontSize
            this.myDiv = fontSizeDiv;
        };
        BodyContainer.prototype.getUIObject = function () {
            return this.myDiv;
        };
        BodyContainer.prototype.setContent = function (content) {
            this.content = content;
            this.content_domObject = this.content.getUIObject();
            this.containerDiv.appendChild(this.content_domObject);
        };
        BodyContainer.prototype.setCollapsed = function () {
            this.containerDiv.style.maxHeight = "0px";
        };
        BodyContainer.prototype.setExpanded = function () {
            throw new Error("Method not implemented.");
        };
        BodyContainer.prototype.startExpandAnimation = function () {
            var timeExpand = 150;
            var timeExpandInSeconds = timeExpand / 1000;
            this.containerDiv.style.transition = "max-height " + timeExpandInSeconds + "s";
            var self = this;
            var expand = function () {
                self.startExpandAnimation_helper();
            };
            var freeMaxHeight = function () {
                self.containerDiv.style.maxHeight = "none";
            };
            window.setTimeout(expand, 1); // one millisecond - for start value of maxHeight
            window.setTimeout(freeMaxHeight, timeExpand);
        };
        BodyContainer.prototype.startExpandAnimation_helper = function () {
            var offsetHeight = this.content_domObject.offsetHeight;
            this.containerDiv.style.maxHeight = offsetHeight + "px";
        };
        BodyContainer.prototype.startCollapseAnimation = function () {
            var offsetHeight = this.content_domObject.offsetHeight;
            this.containerDiv.style.maxHeight = offsetHeight + "px";
            var timeCollapse = 150;
            var timeCollapseInSeconds = timeCollapse / 1000;
            this.containerDiv.style.transition = "max-height " + timeCollapseInSeconds + "s";
            var self = this;
            var collapse = function () {
                self.startCollapseAnimation_helper();
            };
            var end = function () {
                self.onCollapsedAttr.call(self);
            };
            window.setTimeout(collapse, 1); // one millisecond - for start value of maxHeight
            window.setTimeout(end, timeCollapse);
        };
        BodyContainer.prototype.startCollapseAnimation_helper = function () {
            this.containerDiv.style.maxHeight = "0px";
        };
        BodyContainer.prototype.onCollapsed = function (callback) {
            this.onCollapsedAttr = callback;
        };
        return BodyContainer;
    }());
    exports.BodyContainer = BodyContainer;
});
define("visual/HeadContainer", ["require", "exports", "visual/ColorManagement", "visual/general", "visual/Utils"], function (require, exports, ColorManagement_3, general_3, Utils_2) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var HeadContainer = (function () {
        function HeadContainer() {
            this.myDiv = null;
        }
        HeadContainer.prototype.setStyle_NotExpanded = function () {
            this.myDiv.style.borderRadius = general_3.EDGE_RADIUS;
            this.myDiv.style.padding = general_3.STANDARD_PADDING + "px";
            this.myDiv.style.margin = general_3.STANDARD_MARGIN + "px";
            this.myDiv.style.boxShadow = "none";
            this.myDiv.style.backgroundColor = ColorManagement_3.getColorValue(this.backgroundColor);
        };
        HeadContainer.prototype.setMaxWidth = function (maxWidth) {
            this.maxWidth = maxWidth;
            if (this.myDiv != null) {
                this.myDiv.style.maxWidth = (this.maxWidth + 6) + "px";
            }
        };
        HeadContainer.prototype.setStyle_Expanded = function () {
            this.myDiv.style.borderBottomLeftRadius = "0px";
            this.myDiv.style.borderBottomRightRadius = "0px";


			let overlap = 1;
            this.myDiv.style.marginBottom = "-" + overlap + "px"; // head touches body
            this.myDiv.style.paddingBottom = (general_3.STANDARD_MARGIN + general_3.STANDARD_PADDING + overlap) + "px";

			this.myDiv.style.backgroundColor = ColorManagement_3.getColorValue(this.backgroundColor);
            this.myDiv.style.boxShadow = general_3.BOX_SHADOW_NODE;
        };
        HeadContainer.prototype.createUIObject = function () {
            this.myDiv = Utils_2.Utils.getDiv();
            this.myDiv.style.display = general_3.NODE_DISPLAY;
            this.setStyle_NotExpanded();
            if (this.bodyIsAvailableAttr) {
                this.myDiv.style.cursor = "pointer";
                this.myDiv.style.textDecoration = "underline";
            }
            var self = this;
            this.myDiv.onclick = function (ev) {
                if (ev.ctrlKey && ev.shiftKey) {
                    self.eventManager.totalZoomEvent();
                }
                else if (!ev.ctrlKey) {
                    self.eventManager.toggleEvent();
                }
                self.eventManager.focusEvent();
            };
            this.myDiv.oncontextmenu = function (ev) {
                if (ev.ctrlKey) {
                    self.eventManager.zoomOutEvent();
                }
                else {
                    self.eventManager.zoomInEvent();
                }
                ev.preventDefault();
                self.eventManager.focusEvent();
            };
            this.content_domObject = this.content.getUIObject();
            this.myDiv.appendChild(this.content_domObject);
        };
        HeadContainer.prototype.setContent = function (content) {
            this.content = content;
        };
        HeadContainer.prototype.setEventManager = function (eventManager) {
            this.eventManager = eventManager;
        };
        HeadContainer.prototype.setBackgroundColor = function (backgroundColor) {
            this.backgroundColor = backgroundColor;
        };
        HeadContainer.prototype.bodyIsAvailable = function (bool) {
            this.bodyIsAvailableAttr = bool;
        };
        HeadContainer.prototype.isExpanded = function (bool) {
            if (bool) {
                this.setStyle_Expanded();
            }
            else {
                this.setStyle_NotExpanded();
            }
        };
        HeadContainer.prototype.getUIObject = function () {
            if (this.myDiv == null) {
                this.createUIObject();
            }
            return this.myDiv;
        };
        return HeadContainer;
    }());
    exports.HeadContainer = HeadContainer;
});
define("visual/HeadBodyRepresentation", ["require", "exports", "visual/Utils"], function (require, exports, Utils_3) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var HeadBodyRepresentation = (function () {
        function HeadBodyRepresentation() {
            this.bodyIsVisible = false;
        }
        HeadBodyRepresentation.prototype.setHeadContainer = function (headContainer) {
            this.headContainer = headContainer;
        };
        HeadBodyRepresentation.prototype.setBodyContainer_Creator = function (bodyContainer_creator) {
            this.bodyContainer_creator = bodyContainer_creator;
        };
        HeadBodyRepresentation.prototype.removeFromDOM = function () {
            if (this.bodyIsVisible) {
                Utils_3.Utils.remove(this.bodyDiv);
            }
            Utils_3.Utils.remove(this.headContainer.getUIObject());
        };
        HeadBodyRepresentation.prototype.showBody = function () {
            this.bodyContainer = this.bodyContainer_creator.create();
            this.bodyContainer.setCollapsed();
            this.bodyDiv = this.bodyContainer.getUIObject();
            Utils_3.Utils.insertAfter(this.headContainer.getUIObject(), this.bodyDiv);
            var self = this;
            var expand = function () {
                self.bodyContainer.startExpandAnimation();
            };
            var timeLineBreak = 50;
            window.setTimeout(expand, timeLineBreak);
            this.bodyIsVisible = true;
        };
        HeadBodyRepresentation.prototype.hideBody = function () {
            this.bodyContainer.startCollapseAnimation();
            var self = this;
            this.bodyContainer.onCollapsed(function () {
                window.setTimeout(function () {
                    self.removeBody();
                }, 50);
            });
        };
        HeadBodyRepresentation.prototype.removeBody = function () {
            Utils_3.Utils.remove(this.bodyDiv);
            this.headContainer.isExpanded(false);
            this.bodyIsVisible = false;
        };
        HeadBodyRepresentation.prototype.get_bodyIsVisible = function () {
            return this.bodyIsVisible;
        };
        HeadBodyRepresentation.prototype.setMaxWidth = function (maxWidth) {
            this.bodyContainer.setMaxWidth(maxWidth);
        };
        return HeadBodyRepresentation;
    }());
    exports.HeadBodyRepresentation = HeadBodyRepresentation;
});
define("visual/VisualHeadBody", ["require", "exports", "visual/Callbacks", "visual/BodyContainer", "visual/HeadContainer", "visual/HeadBodyRepresentation"], function (require, exports, Callbacks_3, BodyContainer_1, HeadContainer_1, HeadBodyRepresentation_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var VisualHeadBody = (function () {
        function VisualHeadBody() {
            this.myDiv = null;
            this.callbacks = new Callbacks_3.Callbacks();
            this.headContainer = null;
            this.headBodyRepresentation = null;
        }
        VisualHeadBody.prototype.getDataNode = function () {
            return undefined;
        };
        VisualHeadBody.prototype.getCallbacks = function () {
            return this.callbacks;
        };
        VisualHeadBody.prototype.createUIObject = function () {
            this.configureHead();
            this.headContainer = new HeadContainer_1.HeadContainer();
            this.headContainer.setContent(this.getHead());
            this.headContainer.bodyIsAvailable(this.bodyAvailable());
            this.headContainer.setEventManager(this.getEventManager());
            this.headContainer.setBackgroundColor(this.getBackgroundColor());
            this.headContainer.setMaxWidth(this.maxWidth);
            this.myDiv = this.headContainer.getUIObject();
            this.headBodyRepresentation = new HeadBodyRepresentation_1.HeadBodyRepresentation();
            var self = this;
            this.headBodyRepresentation.setBodyContainer_Creator(new (function () {
                function class_1() {
                }
                class_1.prototype.create = function () {
                    var bodyContainer = new BodyContainer_1.BodyContainer(self.getBackgroundColor());
                    self.createBody(self.getMaxWidth());
                    bodyContainer.setContent(self.getBody());
                    bodyContainer.setMaxWidth(self.getMaxWidth());
                    return bodyContainer;
                };
                return class_1;
            }()));
            this.headBodyRepresentation.setHeadContainer(this.headContainer);
        };
        VisualHeadBody.prototype.removeFromDOM = function () {
            this.headBodyRepresentation.removeFromDOM();
        };
        VisualHeadBody.prototype.getUIObject = function () {
            if (this.myDiv === null) {
                this.createUIObject();
            }
            return this.myDiv;
        };
        VisualHeadBody.prototype.showBody = function () {
            this.headBodyRepresentation.showBody();
        };
        VisualHeadBody.prototype.hideBody = function () {
            this.headBodyRepresentation.hideBody();
        };
        VisualHeadBody.prototype.bodyIsVisible = function () {
            if (this.headBodyRepresentation == null) {
                return false;
            }
            else {
                return this.headBodyRepresentation.get_bodyIsVisible();
            }
        };
        VisualHeadBody.prototype.setMaxWidth = function (maxWidth) {
            this.maxWidth = maxWidth;
            if (this.headContainer != null) {
                this.headContainer.setMaxWidth(maxWidth);
            }
            if (this.bodyIsVisible()) {
                this.headBodyRepresentation.setMaxWidth(maxWidth);
            }
        };
        VisualHeadBody.prototype.getMaxWidth = function () {
            return this.maxWidth;
        };
        VisualHeadBody.prototype.configureBody = function () {
            var self = this;
            this.getBody().getCallbacks().onEmitsCursorBottom(function () {
                self.callbacks.emitsCursorBottom();
            });
            this.getBody().getCallbacks().onEmitsCursorTop(function () {
                self.getHead().takeCursorFromBottom();
                self.focus();
            });
        };
        VisualHeadBody.prototype.configureHead = function () {
            var self = this;
            this.getHead().getCallbacks().onEmitsCursorBottom(function () {
                if (self.bodyIsVisible()) {
                    self.getBody().takeCursorFromTop();
                }
                else {
                    self.callbacks.emitsCursorBottom();
                }
            });
            this.getHead().getCallbacks().onEmitsCursorTop(function () {
                self.callbacks.emitsCursorTop();
            });
        };
        VisualHeadBody.prototype.takeCursorFromBottom = function () {
            if (this.bodyIsVisible()) {
                this.getBody().takeCursorFromBottom();
            }
            else {
                this.getHead().takeCursorFromBottom();
                this.focus();
            }
        };
        VisualHeadBody.prototype.focus = function () {
        };
        VisualHeadBody.prototype.removeFocus = function () {
        };
        VisualHeadBody.prototype.takeCursorFromTop = function () {
            this.getHead().takeCursorFromTop();
            this.focus();
        };
        VisualHeadBody.prototype.zoomOutPossible = function () {
            return this.bodyIsVisible();
        };
        VisualHeadBody.prototype.zoomInPossible = function () {
            return undefined;
        };
        VisualHeadBody.prototype.zoomIn = function () {
            if (this.bodyIsVisible()) {
                this.getBody().zoomIn();
            }
            else {
                if (this.bodyAvailable()) {
                    this.showBody();
                    this.headContainer.isExpanded(true);
                }
            }
        };
        VisualHeadBody.prototype.zoomOut = function () {
            if (this.bodyIsVisible()) {
                if (this.getBody().zoomOutPossible()) {
                    this.getBody().zoomOut();
                }
                else {
                    this.hideBody();
                }
            }
        };
        return VisualHeadBody;
    }());
    exports.VisualHeadBody = VisualHeadBody;
});
define("visual/EventManagerForCreateRelationship", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var EventManagerForCreateRelationship = (function () {
        function EventManagerForCreateRelationship(createRelationship) {
            this.createRelationship = createRelationship;
        }
        EventManagerForCreateRelationship.prototype.setParentZoomOutHandler = function (parentZoomOutHandler) {
            this.parentZoomOutHandler = parentZoomOutHandler;
        };
        EventManagerForCreateRelationship.prototype.focusEvent = function () {
            this.createRelationship.focus();
        };
        EventManagerForCreateRelationship.prototype.toggleEvent = function () {
        };
        EventManagerForCreateRelationship.prototype.copyEvent = function () {
        };
        EventManagerForCreateRelationship.prototype.pasteEvent = function () {
            this.createRelationship.paste();
        };
        EventManagerForCreateRelationship.prototype.zoomInEvent = function () {
        };
        EventManagerForCreateRelationship.prototype.zoomOutEvent = function () {
            this.parentZoomOutHandler.zoomOutEvent();
        };
        EventManagerForCreateRelationship.prototype.totalZoomEvent = function () {
        };
        EventManagerForCreateRelationship.prototype.previousEvent = function () {
            this.createRelationship.emitsCursorTop();
        };
        EventManagerForCreateRelationship.prototype.nextEvent = function () {
            this.createRelationship.emitsCursorBottom();
        };
        EventManagerForCreateRelationship.prototype.enterPressed = function () {
            this.createRelationship.confirmAndLeaveWithEnter();
        };
        EventManagerForCreateRelationship.prototype.newChildEvent = function () {
            this.createRelationship.newChild();
        };
        EventManagerForCreateRelationship.prototype.deleteMeEvent = function () {
        };
        EventManagerForCreateRelationship.prototype.confirmEvent = function () {
            this.createRelationship.confirm();
        };
        EventManagerForCreateRelationship.prototype.createLinkEvent = function () {
            console.log("Operation not supported at the moment.");
        };
        return EventManagerForCreateRelationship;
    }());
    exports.EventManagerForCreateRelationship = EventManagerForCreateRelationship;
});
define("visual/CreateRelationship", ["require", "exports", "visual/ColorManagement", "visual/Callbacks", "visual/FocusableTextField", "model/SimpleDataNode", "model/HasDetail", "visual/Clipboard", "visual/EventManagerForCreateRelationship", "visual/Utils", "visual/general"], function (require, exports, ColorManagement_4, Callbacks_4, FocusableTextField_1, SimpleDataNode_2, HasDetail_3, Clipboard_1, EventManagerForCreateRelationship_1, Utils_4, general_4) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var CreateRelationship = (function () {
        function CreateRelationship(placeholderRelationship, simpleVisualNode, backgroundColor) {
            this.zoomStatus = 0;
            this.nodeDiv = null;
            this.callbacks = new Callbacks_4.Callbacks();
            this.placeholderRelationship = placeholderRelationship;
            this.backgroundColor = backgroundColor;
            this.simpleVisualNode = simpleVisualNode;
            this.eventManager = new EventManagerForCreateRelationship_1.EventManagerForCreateRelationship(this);
        }
        CreateRelationship.prototype.newChild = function () {
            var index = this.getOwnIndex();
            this.confirm();
            var node = this.simpleVisualNode.getRelationshipsController().getVisualNodeAtPosition(index);
            node.newChild();
        };
        CreateRelationship.prototype.getCallbacks = function () {
            return this.callbacks;
        };
        CreateRelationship.prototype.getEventManager = function () {
            return undefined;
        };
        CreateRelationship.prototype.setParentZoomOutHandler = function (parentZoomOutHandler) {
        };
        CreateRelationship.prototype.setMaxWidth = function (maxWidth) {
        };
        CreateRelationship.prototype.paste = function () {
            console.log("paste ... CreateRelationship");
            var hasDetail = new HasDetail_3.HasDetail(this.simpleVisualNode.getDataNode(), Clipboard_1.Clipboard.singleton.getDataNode());
            this.replaceCreateRelationshipByConnector(hasDetail);
        };
        CreateRelationship.prototype.confirm = function () {
            var object = SimpleDataNode_2.SimpleDataNode.createInstance(this.getText());
            var hasDetail = HasDetail_3.HasDetail.createInstance(this.simpleVisualNode.getDataNode(), object);
            this.replaceCreateRelationshipByConnector(hasDetail);
        };
        CreateRelationship.prototype.confirmAndLeaveWithEnter = function () {
            var index = this.getOwnIndex();
            this.confirm();
            this.simpleVisualNode.createRelationshipAtPosition(index + 1);
        };
        CreateRelationship.prototype.getOwnIndex = function () {
            return this.simpleVisualNode.getRelationshipsController().getIndexOfChild(this);
        };
        CreateRelationship.prototype.replaceCreateRelationshipByConnector = function (connector) {
            var index = this.getOwnIndex();
            this.simpleVisualNode.getDataNode().replaceRelationshipAtPosition(connector, index);
            this.simpleVisualNode.getRelationshipsController().focusVisualNodeAtPosition(index);
        };
        CreateRelationship.prototype.focus = function () {
            var previousFocused = general_4.getFocusedObject();
            if (previousFocused != null) {
                previousFocused.removeFocus();
            }
            this.nodeDiv.style.backgroundColor = ColorManagement_4.getColorValue(ColorManagement_4.Colors.LightLightBlue);
            general_4.setFocusedObject(this);
        };
        CreateRelationship.prototype.removeFocus = function () {
            this.nodeDiv.style.backgroundColor = ColorManagement_4.getColorValue(this.backgroundColor);
        };
        CreateRelationship.prototype.zoomIn = function () {
        };
        CreateRelationship.prototype.zoomOut = function () {
        };
        CreateRelationship.prototype.getDataNode = function () {
            return this.placeholderRelationship;
        };
        CreateRelationship.prototype.getText = function () {
            return this.head.getText();
        };
        CreateRelationship.prototype.onEnterPressedAtTextField = function (callback) {
            this.onEnterPressedAtTextFieldAttr = callback;
        };
        CreateRelationship.prototype.enterPressedAtTextField = function () {
            this.onEnterPressedAtTextFieldAttr.call(this);
        };
        CreateRelationship.prototype.createUIObject = function () {
            this.nodeDiv = Utils_4.Utils.getDiv();
            this.nodeDiv.style.display = general_4.NODE_DISPLAY;
            this.nodeDiv.style.borderRadius = general_4.EDGE_RADIUS;
            this.nodeDiv.style.padding = general_4.PADING_NODE + "px";
            this.nodeDiv.style.boxShadow = "0px 0px 1px 2px grey, inset 0px 0px 0px 2px grey";
            this.nodeDiv.style.backgroundColor = ColorManagement_4.getColorValue(this.backgroundColor);
            this.head = new FocusableTextField_1.FocusableTextField("", null, this.eventManager);
            this.configureHead();
            var headDiv = this.head.getUIObject();
            headDiv.style.display = general_4.NODE_DISPLAY;
            this.nodeDiv.appendChild(headDiv);
        };
        CreateRelationship.prototype.getUIObject = function () {
            if (this.nodeDiv === null) {
                this.createUIObject();
            }
            return this.nodeDiv;
        };
        CreateRelationship.prototype.configureHead = function () {
            var self = this;
            this.head.onTextChange(function () {
                self.textChanged();
            });
        };
        CreateRelationship.prototype.removeFromDOM = function () {
            Utils_4.Utils.remove(this.nodeDiv);
        };
        CreateRelationship.prototype.textChanged = function () {
            // at the moment: do nothing
        };
        CreateRelationship.prototype.zoomInPossible = function () {
            return false;
        };
        CreateRelationship.prototype.zoomOutPossible = function () {
            if (this.zoomStatus == 0) {
                return false;
            }
            else {
                // TODO
            }
        };
        CreateRelationship.prototype.takeCursorFromTop = function () {
            this.head.takeCursorFromTop();
            this.focus();
        };
        CreateRelationship.prototype.takeCursorFromBottom = function () {
            if (this.zoomStatus == 0) {
                this.head.takeCursorFromBottom();
            }
            else {
                // TODO
            }
            this.focus();
        };
        return CreateRelationship;
    }());
    exports.CreateRelationship = CreateRelationship;
});
define("visual/EventManagerForSimpleVisualNode", ["require", "exports", "visual/Clipboard", "loadApp", "model/IDManager", "model/ExportImport", "model/HasDetail"], function (require, exports, Clipboard_2, loadApp_1, IDManager_7, ExportImport_1, HasDetail_4) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var EventManagerForSimpleVisualNode = (function () {
        function EventManagerForSimpleVisualNode(simpleVisualNode, headBody) {
            this.simpleVisualNode = simpleVisualNode;
            this.dataNode = simpleVisualNode.getDataNode();
            this.headBody = headBody;
        }
        EventManagerForSimpleVisualNode.prototype.exportObjectEvent = function () {
            var jsonObject = ExportImport_1.getExportAsJson_Object(this.dataNode);
            var text = JSON.stringify(jsonObject);
            loadApp_1.setContentOfTextArea(text);
        };
        EventManagerForSimpleVisualNode.prototype.importToObjectEvent = function () {
            var tmpIdManager = new IDManager_7.IDManager();
            ExportImport_1.getDataNodes(JSON.parse(loadApp_1.textArea.value), tmpIdManager);
            IDManager_7.IDManager.singleton.import(tmpIdManager);
            var hasDetail = HasDetail_4.HasDetail.createInstance(this.dataNode, tmpIdManager.getRootNode());
            this.simpleVisualNode.getDataNode().addRelationship(hasDetail);
        };
        EventManagerForSimpleVisualNode.prototype.setParentZoomOutHandler = function (parentZoomOutHandler) {
            this.parentZoomOutHandler = parentZoomOutHandler;
        };
        EventManagerForSimpleVisualNode.prototype.focusEvent = function () {
            this.simpleVisualNode.focus();
        };
        EventManagerForSimpleVisualNode.prototype.toggleEvent = function () {
            if (this.headBody.bodyIsVisible()) {
                this.headBody.zoomOut();
            }
            else {
                this.headBody.zoomIn();
            }
        };
        EventManagerForSimpleVisualNode.prototype.copyEvent = function () {
            Clipboard_2.Clipboard.singleton.putIntoClipboard(this.dataNode);
        };
        EventManagerForSimpleVisualNode.prototype.pasteEvent = function () {
            console.log("pasteEvent on SimpleVisualNode not possible at the moment");
        };
        EventManagerForSimpleVisualNode.prototype.zoomInEvent = function () {
            this.headBody.zoomIn();
        };
        EventManagerForSimpleVisualNode.prototype.zoomOutEvent = function () {
            if (this.headBody.zoomOutPossible()) {
                this.headBody.zoomOut();
                this.headBody.getHead().takeCursorFromBottom(); // the object, that consumes the zoomEvent gets the focus ...
                this.headBody.focus();
            }
            else {
                this.parentZoomOutHandler.zoomOutEvent();
            }
        };
        EventManagerForSimpleVisualNode.prototype.totalZoomEvent = function () {
            IDManager_7.IDManager.singleton.setRootNode(this.dataNode);
            loadApp_1.updateVisualDataNodeView();
        };
        EventManagerForSimpleVisualNode.prototype.previousEvent = function () {
            // this.simpleVisualNode.emitsCursorTop();
        };
        EventManagerForSimpleVisualNode.prototype.nextEvent = function () {
            // this.simpleVisualNode.emitsCursorBottom();
        };
        EventManagerForSimpleVisualNode.prototype.enterPressed = function () {
            this.simpleVisualNode.getCallbacks().leavesWithEnter();
        };
        EventManagerForSimpleVisualNode.prototype.newChildEvent = function () {
            this.simpleVisualNode.newChild();
        };
        EventManagerForSimpleVisualNode.prototype.deleteMeEvent = function () {
            this.simpleVisualNode.getCallbacks().delete();
        };
        EventManagerForSimpleVisualNode.prototype.confirmEvent = function () {
            console.log("ConfirmEvent on SimpleVisualNode is not defined!");
        };
        EventManagerForSimpleVisualNode.prototype.createLinkEvent = function () {
            console.log("Operation not supported. It is not possible to create link on simpleVisualNode.");
        };
        return EventManagerForSimpleVisualNode;
    }());
    exports.EventManagerForSimpleVisualNode = EventManagerForSimpleVisualNode;
});
define("visual/EventManagerForNamedLink", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var EventManagerForNamedLink = (function () {
        function EventManagerForNamedLink(namedLinkVisualNode, headBody) {
            this.namedLinkVisualNode = namedLinkVisualNode;
            this.dataNode = namedLinkVisualNode.getDataNode();
            this.headBody = headBody;
        }
        EventManagerForNamedLink.prototype.setParentZoomOutHandler = function (parentZoomOutHandler) {
            this.parentZoomOutHandler = parentZoomOutHandler;
        };
        EventManagerForNamedLink.prototype.focusEvent = function () {
        };
        EventManagerForNamedLink.prototype.toggleEvent = function () {
            if (this.headBody.bodyIsVisible()) {
                this.headBody.zoomOut();
            }
            else {
                this.headBody.zoomIn();
            }
        };
        EventManagerForNamedLink.prototype.copyEvent = function () {
        };
        EventManagerForNamedLink.prototype.pasteEvent = function () {
        };
        EventManagerForNamedLink.prototype.zoomInEvent = function () {
            this.headBody.zoomIn();
        };
        EventManagerForNamedLink.prototype.zoomOutEvent = function () {
            if (this.headBody.zoomOutPossible()) {
                this.headBody.zoomOut();
                this.headBody.getHead().takeCursorFromBottom(); // the object, that consumes the zoomEvent gets the focus ...
                this.headBody.focus();
            }
            else {
                this.parentZoomOutHandler.zoomOutEvent();
            }
        };
        EventManagerForNamedLink.prototype.totalZoomEvent = function () {
        };
        EventManagerForNamedLink.prototype.previousEvent = function () {
        };
        EventManagerForNamedLink.prototype.nextEvent = function () {
        };
        EventManagerForNamedLink.prototype.enterPressed = function () {
            this.namedLinkVisualNode.getCallbacks().leavesWithEnter();
        };
        EventManagerForNamedLink.prototype.newChildEvent = function () {
        };
        EventManagerForNamedLink.prototype.deleteMeEvent = function () {
            this.namedLinkVisualNode.getCallbacks().delete();
        };
        EventManagerForNamedLink.prototype.confirmEvent = function () {
        };
        EventManagerForNamedLink.prototype.createLinkEvent = function () {
        };
        return EventManagerForNamedLink;
    }());
    exports.EventManagerForNamedLink = EventManagerForNamedLink;
});
define("visual/NamedLinkVisualNode", ["require", "exports", "visual/ColorManagement", "visual/VisualHeadBody", "visual/EventManagerForNamedLink", "visual/FocusableTextField", "model/SimpleDataNode", "visual/SimpleVisualNode"], function (require, exports, ColorManagement_5, VisualHeadBody_1, EventManagerForNamedLink_1, FocusableTextField_2, SimpleDataNode_3, SimpleVisualNode_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var NamedLinkVisualNode = (function (_super) {
        __extends(NamedLinkVisualNode, _super);
        function NamedLinkVisualNode(dataNode, backgroundColor) {
            var _this = _super.call(this) || this;
            _this.dataNode = dataNode;
            _this.backgroundColor = backgroundColor;
            var self = _this;
            dataNode.register({
                notify: function (action, object, position) {
                    self.dataNodeChanged(action, object, position);
                }
            });
            _this.eventManager = new EventManagerForNamedLink_1.EventManagerForNamedLink(_this, _this);
            _this.head = new FocusableTextField_2.FocusableTextField(_this.getDataNode().getName(), backgroundColor, _this.eventManager);
            _this.head.setFontColor(ColorManagement_5.Colors.Grey);
            return _this;
        }
        NamedLinkVisualNode.prototype.getEventManager = function () {
            return this.eventManager;
        };
        NamedLinkVisualNode.prototype.setParentZoomOutHandler = function (parentZoomOutHandler) {
            this.eventManager.setParentZoomOutHandler(parentZoomOutHandler);
        };
        NamedLinkVisualNode.prototype.getBackgroundColor = function () {
            return this.backgroundColor;
        };
        NamedLinkVisualNode.prototype.createBody = function () {
            this.createRelatedVisualNode();
        };
        NamedLinkVisualNode.prototype.bodyAvailable = function () {
            return this.dataNode.getTo() != null;
        };
        NamedLinkVisualNode.prototype.getHead = function () {
            return this.head;
        };
        NamedLinkVisualNode.prototype.getBody = function () {
            return this.relatedVisualNode;
        };
        NamedLinkVisualNode.prototype.newChild = function () {
            console.log("not implemented");
        };
        NamedLinkVisualNode.prototype.dataNodeChanged = function (action, object, position) {
        };
        NamedLinkVisualNode.prototype.getDataNode = function () {
            return this.dataNode;
        };
        NamedLinkVisualNode.prototype.getVisualNodeForDataNode = function (dataNode) {
            var visualNode;
            var backgroundColor = ColorManagement_5.getColorForChild(this.backgroundColor);
            var parentZoomOutHandler = this.eventManager;
            if (dataNode instanceof SimpleDataNode_3.SimpleDataNode) {
                visualNode = new SimpleVisualNode_1.SimpleVisualNode(dataNode, backgroundColor); // automatic cast (dataNode)
                visualNode.setParentZoomOutHandler(parentZoomOutHandler);
            }
            else {
                console.log("VisualNode not implemented");
            }
            return visualNode;
        };
        NamedLinkVisualNode.prototype.configureRelatedVisualNode = function () {
            var self = this;
            this.relatedVisualNode.getCallbacks().onLeavesWithEnter(function () {
                self.getCallbacks().leavesWithEnter();
            });
        };
        NamedLinkVisualNode.prototype.createRelatedVisualNode = function () {
            this.relatedVisualNode = this.getVisualNodeForDataNode(this.dataNode.getTo());
            this.configureRelatedVisualNode();
        };
        return NamedLinkVisualNode;
    }(VisualHeadBody_1.VisualHeadBody));
    exports.NamedLinkVisualNode = NamedLinkVisualNode;
});
define("visual/SimpleVisualNode", ["require", "exports", "model/SimpleDataNode", "visual/ColorManagement", "visual/FocusableTextField", "visual/ListController", "model/PlaceholderRelationship", "visual/CreateRelationship", "model/HasDetail", "model/observe", "visual/VisualHeadBody", "visual/EventManagerForSimpleVisualNode", "model/DataTypes", "visual/NamedLinkVisualNode"], function (require, exports, SimpleDataNode_4, ColorManagement_6, FocusableTextField_3, ListController_1, PlaceholderRelationship_2, CreateRelationship_1, HasDetail_5, observe_4, VisualHeadBody_2, EventManagerForSimpleVisualNode_1, DataTypes_3, NamedLinkVisualNode_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var SimpleVisualNode = (function (_super) {
        __extends(SimpleVisualNode, _super);
        function SimpleVisualNode(dataNode, backgroundColor) {
            var _this = _super.call(this) || this;
            _this.dataNode = dataNode;
            _this.backgroundColor = backgroundColor;
            var self = _this;
            _this.dataNode.register({
                notify: function (action, object, position) {
                    self.dataNodeChanged(action, object, position);
                }
            });
            _this.eventManager = new EventManagerForSimpleVisualNode_1.EventManagerForSimpleVisualNode(_this, _this);
            _this.head = new FocusableTextField_3.FocusableTextField(_this.dataNode.getName(), _this.backgroundColor, _this.eventManager);
            _this.configureTextField();
            return _this;
        }
        SimpleVisualNode.prototype.configureTextField = function () {
            var self = this;
            this.head.onTextChange(function () {
                // update simpleDataNode
                self.textFieldChanged();
            });
        };
        SimpleVisualNode.prototype.getRelationshipsController = function () {
            return this.relationshipsController;
        };
        SimpleVisualNode.prototype.setParentZoomOutHandler = function (parentZoomOutHandler) {
            this.eventManager.setParentZoomOutHandler(parentZoomOutHandler);
        };
        SimpleVisualNode.prototype.getHead = function () {
            return this.head;
        };
        SimpleVisualNode.prototype.getBody = function () {
            if (this.relationshipsController == null) {
                this.createBody(this.getMaxWidth());
            }
            return this.relationshipsController;
        };
        SimpleVisualNode.prototype.createBody = function (maxWidth) {
            this.createRelationshipController(maxWidth);
        };
        SimpleVisualNode.prototype.createRelationshipController = function (maxWidth) {
            var relationships = [];
            for (var i = 0; i < this.dataNode.getRelationships().length; i++) {
                var currentRelationship = this.dataNode.getRelationships()[i];
                var visualRelationship = this.getVisualNodeForDataNode(currentRelationship);
                relationships[i] = visualRelationship;
            }
            this.relationshipsController = new ListController_1.ListController(relationships, maxWidth);
            this.configureRelationshipsController();
        };
        SimpleVisualNode.prototype.deleteRelationshipController = function () {
            this.hideBody();
        };
        SimpleVisualNode.prototype.bodyAvailable = function () {
            return this.dataNode.getRelationships().length > 0;
        };
        SimpleVisualNode.prototype.newChild = function () {
            this.dataNode.addRelationshipAtPosition(PlaceholderRelationship_2.PlaceholderRelationship.createInstance(), 0);
            if (!this.bodyIsVisible()) {
                this.zoomIn();
            }
            this.relationshipsController.takeCursorFromTop();
        };
        SimpleVisualNode.prototype.configureRelationshipsController = function () {
            var self = this;
            this.relationshipsController.onChildLeavesWithEnter(function (listElem) {
                self.relationshipsController_childLeavesWithEnter(listElem);
            });
        };
        SimpleVisualNode.prototype.relationshipsController_childLeavesWithEnter = function (listElem) {
            var indexForNewRelationship = 1 + this.relationshipsController.getIndexOfChild(listElem);
            this.createRelationshipAtPosition(indexForNewRelationship);
        };
        SimpleVisualNode.prototype.createRelationshipAtPosition = function (position) {
            this.dataNode.addRelationshipAtPosition(PlaceholderRelationship_2.PlaceholderRelationship.createInstance(), position);
            this.relationshipsController.focusVisualNodeAtPosition(position);
        };
        SimpleVisualNode.prototype.getDataNode = function () {
            return this.dataNode;
        };
        SimpleVisualNode.prototype.dataNodeChanged = function (action, object, position) {
            if (action === observe_4.ObActions.ChangedName) {
                var currentName = this.head.getText();
                var newName = this.dataNode.getName();
                if (currentName != newName) {
                    this.head.setText(newName);
                }
            }
            else if (action === observe_4.ObActions.RemovedRelationship) {
                if (this.bodyIsVisible()) {
                    this.relationshipsController.removeVisualNodeAtPosition(position);
                    if (this.dataNode.getRelationships().length == 0) {
                        this.deleteRelationshipController();
                    }
                }
            }
            else if (action === observe_4.ObActions.AddedRelationship) {
                if (this.bodyIsVisible()) {
                    var visualRelationship = this.getVisualNodeForDataNode(object);
                    this.relationshipsController.insertVisualNodeAtPosition(visualRelationship, position);
                }
            }
            else if (action === observe_4.ObActions.ReplacedRelationship) {
                if (this.bodyIsVisible()) {
                    var visualRelationship = this.getVisualNodeForDataNode(object);
                    this.relationshipsController.removeVisualNodeAtPosition(position);
                    this.relationshipsController.insertVisualNodeAtPosition(visualRelationship, position);
                }
            }
        };
        SimpleVisualNode.prototype.getVisualNodeForDataNode = function (dataNode) {
            var visualNode;
            if (dataNode instanceof PlaceholderRelationship_2.PlaceholderRelationship) {
                visualNode = this.getCreateRelationship(dataNode);
            }
            else {
                var backgroundColor = ColorManagement_6.getColorForChild(this.backgroundColor);
                var parentZoomOutHandler = this.eventManager;
                if (dataNode instanceof SimpleDataNode_4.SimpleDataNode) {
                    visualNode = new SimpleVisualNode(dataNode, backgroundColor); // automatic cast (dataNode)
                    visualNode.setParentZoomOutHandler(parentZoomOutHandler);
                }
                else if (dataNode instanceof HasDetail_5.HasDetail) {
                    visualNode = this.getVisualNodeForDataNode(dataNode.getObject());
                }
                else if (dataNode.getType() === DataTypes_3.DataTypes.NamedLinkType) {
                    var relationshipVisualNode = new NamedLinkVisualNode_1.NamedLinkVisualNode(dataNode, backgroundColor);
                    relationshipVisualNode.setParentZoomOutHandler(parentZoomOutHandler);
                    visualNode = relationshipVisualNode;
                }
                else {
                    console.log("VisualNode not implemented");
                }
            }
            var self = this;
            visualNode.getCallbacks().onDelete(function () {
                self.deleteVisualNode(visualNode);
            });
            return visualNode;
        };
        SimpleVisualNode.prototype.deleteVisualNode = function (visualNode) {
            var index = this.relationshipsController.getIndexOfChild(visualNode);
            var relationship = this.dataNode.getRelationships()[index];
            if (relationship instanceof HasDetail_5.HasDetail) {
                relationship.delete();
                if (index > 0) {
                    this.relationshipsController.getVisualNodeAtPosition(index - 1).takeCursorFromBottom();
                }
                else {
                    this.getHead().takeCursorFromBottom();
                }
            }
            else if (relationship.getType() === DataTypes_3.DataTypes.NamedLinkType) {
                this.dataNode.deleteRelationship(relationship);
                if (index > 0) {
                    this.relationshipsController.getVisualNodeAtPosition(index - 1).takeCursorFromBottom();
                }
                else {
                    this.getHead().takeCursorFromBottom();
                }
            }
        };
        SimpleVisualNode.prototype.getCreateRelationship = function (placeHolderRelationship) {
            var createRelationship = new CreateRelationship_1.CreateRelationship(placeHolderRelationship, this, ColorManagement_6.getColorForChild(this.backgroundColor));
            return createRelationship;
        };
        SimpleVisualNode.prototype.textFieldChanged = function () {
            this.dataNode.setName(this.head.getText());
        };
        SimpleVisualNode.prototype.getBackgroundColor = function () {
            return this.backgroundColor;
        };
        SimpleVisualNode.prototype.getEventManager = function () {
            return this.eventManager;
        };
        return SimpleVisualNode;
    }(VisualHeadBody_2.VisualHeadBody));
    exports.SimpleVisualNode = SimpleVisualNode;
});
define("visual/CreateSampleData", ["require", "exports", "model/SimpleDataNode", "model/TextObject", "model/NamedLink", "model/ExportImport", "model/IDManager"], function (require, exports, SimpleDataNode_5, TextObject_1, NamedLink_2, ExportImport_2, IDManager_8) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var CSD = null;
    exports.CSD = CSD;
});
define("loadApp", ["require", "exports", "model/ExportImport", "visual/SimpleVisualNode", "visual/ColorManagement", "model/IDManager", "visual/CreateSampleData", "visual/Utils", "visual/general"], function (require, exports, ExportImport_3, SimpleVisualNode_2, ColorManagement_7, IDManager_9, CreateSampleData_1, Utils_5, general_5) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    function loadApp() {
        loadSampleData();
        createVisualDataNodeView();
        createTestDiv();
        document.body.appendChild(exports.testDiv);
        document.body.appendChild(exports.visualDataNodeView);
        appendPlaceholder();
        appendTmpField();
        document.body.style.margin = "0";
        document.body.style.backgroundColor = ColorManagement_7.getColorValue(backgroundColor);
        updateVisualDataNodeView();
        adaptToWindowSize();
        window.addEventListener("resize", function () {
            adaptToWindowSize();
        });
    }
    exports.loadApp = loadApp;
    function loadSampleData() {
        var rootNode = new CreateSampleData_1.CSD().getSimpleNamedLink();
        IDManager_9.IDManager.singleton.setRootNode(rootNode);
    }
    function loadJsonData() {
        var rootNode = new CreateSampleData_1.CSD().loadJsonData();
    }
    function getWindowWidth() {
        return window.innerWidth - 80;
    }
    function adaptToWindowSize() {
        var width = getWindowWidth();
        var elem = exports.visualDataNodeView;
        var marginLeft;
        var newWidth;
        if (width > general_5.MAX_WIDTH_OF_NODE_VIEW) {
            newWidth = general_5.MAX_WIDTH_OF_NODE_VIEW;
            marginLeft = (width - general_5.MAX_WIDTH_OF_NODE_VIEW) / 2;
        }
        else {
            newWidth = width;
            marginLeft = 0;
        }
        elem.style.width = newWidth + "px";
        elem.style.marginLeft = marginLeft + "px";
        visualRootNode.setMaxWidth(newWidth);

        var height = window.innerHeight - 30;
        placeholder.style.height = height + "px";
    }
    function createVisualDataNodeView() {
        exports.visualDataNodeView = Utils_5.Utils.getDiv();
        exports.visualDataNodeView.style.display = general_5.NODE_DISPLAY;
        exports.visualDataNodeView.style.paddingLeft = "20px";
        exports.visualDataNodeView.style.paddingRight = "20px";
        exports.visualDataNodeView.style.paddingTop = "50px";
    }
    function appendPlaceholder() {
        document.body.appendChild(placeholder);
    }
    exports.appendPlaceholder = appendPlaceholder;
    function updateVisualDataNodeView() {
        while (exports.visualDataNodeView.hasChildNodes()) {
            exports.visualDataNodeView.removeChild(exports.visualDataNodeView.lastChild);
        }
        var simpleDataNode = IDManager_9.IDManager.singleton.getRootNode();
        visualRootNode = new SimpleVisualNode_2.SimpleVisualNode(simpleDataNode, 0);
        visualRootNode.setMaxWidth(Math.min(general_5.MAX_WIDTH_OF_NODE_VIEW, getWindowWidth()) - 19);
        var uiObject = visualRootNode.getUIObject();
        exports.visualDataNodeView.appendChild(uiObject);
        visualRootNode.takeCursorFromTop();
        visualRootNode.zoomIn();
    }
    exports.updateVisualDataNodeView = updateVisualDataNodeView;
    function createTestDiv() {
        exports.testDiv = Utils_5.Utils.getDiv();
        exports.textArea = document.createElement("textarea");
        exports.testDiv.appendChild(createTestButton());
        exports.testDiv.appendChild(createExportButton());
        exports.testDiv.appendChild(createImportButton());
        exports.testDiv.appendChild(exports.textArea);
        exports.testDiv.style.backgroundColor = "lightgreen";
    }
    function createTestButton() {
        var button = document.createElement('input');
        button.type = 'button';
        button.value = "Start test";
        button.addEventListener("click", function () {
            alert("Test");
        });
        return button;
    }
    function createExportButton() {
        var button = document.createElement('input');
        button.type = 'button';
        button.value = "Export";
        button.addEventListener("click", function () {
            var jsonString = JSON.stringify(ExportImport_3.getExportAsJson());
            exports.textArea.value = jsonString;
        });
        return button;
    }
    function setContentOfTextArea(text) {
        exports.textArea.value = text;
    }
    exports.setContentOfTextArea = setContentOfTextArea;
    function createImportButton() {
        var button = document.createElement('input');
        button.type = 'button';
        button.value = "Import";
        button.addEventListener("click", function () {
            var jsonString = exports.textArea.value;
            ExportImport_3.getDataNodes(JSON.parse(jsonString), IDManager_9.IDManager.singleton);
            updateVisualDataNodeView();
        });
        return button;
    }
    function appendTmpField() {
        exports.tmpField = document.createElement("div");
        document.body.appendChild(exports.tmpField);
    }
    function loadAppFromJSON(jsonObject) {
        ExportImport_3.getDataNodes(jsonObject, IDManager_9.IDManager.singleton);
        createVisualDataNodeView();
        document.body.appendChild(exports.visualDataNodeView);
        appendTmpField();
        appendPlaceholder();
        document.body.style.margin = "0";
        document.body.style.backgroundColor = ColorManagement_7.getColorValue(backgroundColor);
        updateVisualDataNodeView();
        adaptToWindowSize();
        window.addEventListener("resize", function () {
            adaptToWindowSize();
        });
    }
    exports.loadAppFromJSON = loadAppFromJSON;
    var visualRootNode;
    var placeholder = document.createElement("div");
    var backgroundColor = ColorManagement_7.Colors.White;
});
define("tests", ["require", "exports", "general/List", "loadApp", "visual/TextField", "visual/BodyContainer"], function (require, exports, List_2, loadApp_2, TextField_2, BodyContainer_2) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    function runTests() {
        new Tests().testList();
    }
    exports.runTests = runTests;
    var Tests = (function () {
        function Tests() {
        }
        Tests.prototype.testBody = function () {
            var body = new BodyContainer_2.BodyContainer(null);
            body.setContent(new TextField_2.TextField("", null));
            loadApp_2.tmpField.appendChild(body.getUIObject());
            body.startExpandAnimation();
        };
        Tests.prototype.testTextField = function () {
            var textField = new TextField_2.TextField("test FocusableTextField", null);
            loadApp_2.tmpField.appendChild(textField.getUIObject());
            textField.onTextChange(function () {
                console.log("text changed - " + textField.getText());
            });
            var newText = "newText";
            textField.setText(newText);
            this.assert(textField.getText() === newText);
        };
        Tests.prototype.testList = function () {
            var list = new List_2.List();
            var iNull = "iNull";
            var iOne = "iOne";
            var iTwo = "iTwo";
            list.insert(iNull, 0);
            list.insert(iOne, 1);
            list.insert(iTwo, 2);
            // getNext()
            this.assert(list.getNext(iNull) === iOne);
            // getPrevious()
            this.assert(list.getPrevious(iTwo) == iOne);
            // getIndex()
            this.assert(list.getIndex(iOne) == 1);
            // insert at the end
            list.insert("c", 3);
            this.assert(list.get(3).indexOf("c") == 0);
            // insert in the middle
            list.insert("b", 2);
            this.assert(list.get(2).indexOf("b") == 0);
            // insert at the beginning
            list.insert("a", 0);
            this.assert(list.get(0).indexOf("a") == 0);
            // remove
            list = new List_2.List();
            list.insert("iNull", 0);
            list.insert("iOne", 1);
            list.insert("iTwo", 2);
            list.remove(1);
            this.assert(list.get(1).indexOf("iTwo") == 0);
        };
        Tests.prototype.assert = function (boolValue) {
            if (boolValue) {
                console.log("passed");
            }
            else {
                console.log("!!! error !!!");
            }
        };
        return Tests;
    }());
    exports.Tests = Tests;
});
define("exporter/data", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.jsonData = { };
});
define("general/ILogger", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
});
define("general/I_UIObject", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
});
define("general/DisplayLogger", ["require", "exports", "visual/Utils"], function (require, exports, Utils_6) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var DisplayLogger = (function () {
        function DisplayLogger() {
            this.myDiv = Utils_6.Utils.getDiv();
        }
        DisplayLogger.prototype.getUIObject = function () {
            return this.myDiv;
        };
        DisplayLogger.prototype.log = function (toLog) {
            var toLog_Div = Utils_6.Utils.getDiv();
            toLog_Div.style.borderBottom = "dotted";
            toLog_Div.innerHTML = toLog;
            this.myDiv.appendChild(toLog_Div);
        };
        return DisplayLogger;
    }());
    exports.DisplayLogger = DisplayLogger;
});
define("general/IDManager_New", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var IDManager_New = (function (_super) {
        __extends(IDManager_New, _super);
        function IDManager_New() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            _this.highestID = -1;
            return _this;
        }
        IDManager_New.prototype.getNewID = function () {
            this.highestID++;
            var toReturn = this.highestID;
            return toReturn;
        };
        IDManager_New.prototype.remove = function (key) {
            // TODO free this key
            _super.prototype.delete.call(this, key);
        };
        return IDManager_New;
    }(Map));
    exports.IDManager_New = IDManager_New;
});
define("general/Interfaces/GenericObserver", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
});
define("general/observe/GenericObAction", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var GenericObActions;
    (function (GenericObActions) {
        GenericObActions[GenericObActions["AddedObject"] = 0] = "AddedObject";
        GenericObActions[GenericObActions["RemovedObject"] = 1] = "RemovedObject";
        GenericObActions[GenericObActions["ReplacedObject"] = 2] = "ReplacedObject";
    })(GenericObActions = exports.GenericObActions || (exports.GenericObActions = {}));
});
define("general/observe/GenericObservable", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var GenericObservable = (function () {
        function GenericObservable() {
            this.observers = [];
        }
        GenericObservable.prototype.register = function (observer) {
            this.observers.push(observer);
        };
        GenericObservable.prototype.unregister = function (observer) {
            var n = this.observers.indexOf(observer);
            this.observers.splice(n, 1);
        };
        GenericObservable.prototype.notify = function (notifyObject) {
            var i, max;
            for (i = 0, max = this.observers.length; i < max; i += 1) {
                this.observers[i].notify(notifyObject);
            }
        };
        return GenericObservable;
    }());
    exports.GenericObservable = GenericObservable;
});
define("general/observe/ListNotifier", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var ListNotifier = (function () {
        function ListNotifier() {
        }
        return ListNotifier;
    }());
    exports.ListNotifier = ListNotifier;
});
define("general/observe/NoNotifyObjectType_Observable", ["require", "exports", "general/observe/GenericObservable"], function (require, exports, GenericObservable_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var NoNotifyObjectType_Observable = (function (_super) {
        __extends(NoNotifyObjectType_Observable, _super);
        function NoNotifyObjectType_Observable() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        NoNotifyObjectType_Observable.prototype.notify = function () {
            _super.prototype.notify.call(this, null);
        };
        return NoNotifyObjectType_Observable;
    }(GenericObservable_1.GenericObservable));
    exports.NoNotifyObjectType_Observable = NoNotifyObjectType_Observable;
});
define("general/observe/ObservableList", ["require", "exports", "model/observe", "general/List"], function (require, exports, observe_5, List_3) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var ObservableList = (function (_super) {
        __extends(ObservableList, _super);
        function ObservableList() {
            var _this = _super.call(this) || this;
            _this.list = new List_3.List();
            return _this;
        }
        // It is allowed that position == length. (that means toInsert is appended to the list)
        ObservableList.prototype.insert = function (toInsert, position) {
            this.list.insert(toInsert, position);
            var notifyObject = new observe_5.ListNotifier();
            notifyObject.position = position;
            notifyObject.object = toInsert;
            notifyObject.action = observe_5.GenericObActions.AddedObject;
            this.notify(notifyObject);
        };
        ObservableList.prototype.remove = function (position) {
            this.list.remove(position);
            var notifyObject = new observe_5.ListNotifier();
            notifyObject.position = position;
            notifyObject.object = null;
            notifyObject.action = observe_5.GenericObActions.RemovedObject;
            this.notify(notifyObject);
        };
        ObservableList.prototype.get = function (position) {
            return this.list.get(position);
        };
        ObservableList.prototype.getIndex = function (object) {
            return this.list.getIndex(object);
        };
        ObservableList.prototype.getNext = function (object) {
            return this.list.getNext(object);
        };
        ObservableList.prototype.getPrevious = function (object) {
            return this.list.getPrevious(object);
        };
        ObservableList.prototype.getLength = function () {
            return this.list.getLength();
        };
        return ObservableList;
    }(observe_5.GenericObservable));
    exports.ObservableList = ObservableList;
});
define("general/observe/ObservableString", ["require", "exports", "general/observe/NoNotifyObjectType_Observable"], function (require, exports, NoNotifyObjectType_Observable_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var Observable_String_Data = (function (_super) {
        __extends(Observable_String_Data, _super);
        function Observable_String_Data() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        Observable_String_Data.prototype.set = function (toSet) {
            this.myString = toSet;
            this.notify();
        };
        Observable_String_Data.prototype.get = function () {
            return this.myString;
        };
        return Observable_String_Data;
    }(NoNotifyObjectType_Observable_1.NoNotifyObjectType_Observable));
    exports.Observable_String_Data = Observable_String_Data;
});
define("model/A_DataNode", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var A_DataNode = (function () {
        function A_DataNode() {
        }
        A_DataNode.prototype.getDataNodeId = function () {
            return this.dataNodeId;
        };
        A_DataNode.prototype.setDataNodeId = function (id) {
            this.dataNodeId = id;
        };
        A_DataNode.prototype.getTypInformation = function () {
            return this.typInformation;
        };
        A_DataNode.prototype.setTypInformation = function (typInformation) {
            this.typInformation = typInformation;
        };
        return A_DataNode;
    }());
    exports.A_DataNode = A_DataNode;
});
define("model/DataNode_Provider_OldID", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var DataNode_Provider_OldID = (function () {
        function DataNode_Provider_OldID(idManager, idMapper) {
            this._idManager = idManager;
            this._idMapper = idMapper;
        }
        DataNode_Provider_OldID.prototype.get = function (key) {
            return this._idManager.get(this._idMapper.get(key));
        };
        DataNode_Provider_OldID.prototype.set = function (key, value) {
            throw new Error("Method not implemented.");
        };
        DataNode_Provider_OldID.prototype.delete = function (key) {
            throw new Error("Method not implemented.");
        };
        return DataNode_Provider_OldID;
    }());
    exports.DataNode_Provider_OldID = DataNode_Provider_OldID;
});
define("model/TypInformations", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.SIMPLE_DATA_NODE_TYP = "SimpleDataNode_Typ";
});
define("model/Interfaces/I_DataNode_Generator", ["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
});
define("model/SimpleDataNode_Generator", ["require", "exports", "model/SimpleDataNode"], function (require, exports, SimpleDataNode_6) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var SimpleDataNode_Generator = (function () {
        function SimpleDataNode_Generator() {
        }
        SimpleDataNode_Generator.prototype.complete = function (provider) {
            var relationshipsJSON = this.json.relationships;
            for (var i = 0; i < relationshipsJSON.length; i++) {
                var currentID = relationshipsJSON[i];
                var currentRelationship = provider.get(currentID);
                this.simpleDataNode.addRelationshipAtPosition(currentRelationship, i);
            }
        };
        SimpleDataNode_Generator.prototype.createStub = function () {
            this.simpleDataNode = new SimpleDataNode_6.SimpleDataNode(this.json.name);
            return this.simpleDataNode;
        };
        SimpleDataNode_Generator.prototype.setJSON = function (json) {
            this.json = json;
        };
        return SimpleDataNode_Generator;
    }());
    exports.SimpleDataNode_Generator = SimpleDataNode_Generator;
});
define("model/Generator_Provider", ["require", "exports", "model/TypInformations", "model/SimpleDataNode_Generator"], function (require, exports, TypInformations_1, SimpleDataNode_Generator_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var Generator_Provider = (function () {
        function Generator_Provider() {
            this.generatorProvider.set(TypInformations_1.SIMPLE_DATA_NODE_TYP, function () {
                return new SimpleDataNode_Generator_1.SimpleDataNode_Generator;
            });
        }
        Generator_Provider.prototype.get = function (typInformation) {
            return this.generatorProvider.get(typInformation)();
        };
        return Generator_Provider;
    }());
    exports.Generator_Provider = Generator_Provider;
});
define("model/JSON_To_DataNodes", ["require", "exports", "model/Generator_Provider", "model/DataNode_Provider_OldID"], function (require, exports, Generator_Provider_1, DataNode_Provider_OldID_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var JSON_To_DataNodes = (function () {
        function JSON_To_DataNodes(listOfDataNodes, iDManager) {
            this.generatorProvider = new Generator_Provider_1.Generator_Provider();
            this.iDManager = iDManager;
            this._iDMapper = new Map();
            this.listOfDataNodes = listOfDataNodes;
            this.listOfGenerators = [];
        }
        JSON_To_DataNodes.prototype.createDataNodes = function () {
            for (var i = 0; i < this.listOfDataNodes.length; i++) {
                this.handle(this.listOfDataNodes[i]);
            }
            var dataNodeProviderOldID = new DataNode_Provider_OldID_1.DataNode_Provider_OldID(this.iDManager, this._iDMapper);
            for (var i = 0; i < this.listOfGenerators.length; i++) {
                this.listOfGenerators[i].complete(dataNodeProviderOldID);
            }
        };
        JSON_To_DataNodes.prototype.handle = function (jsonObject) {
            var generator = this.generatorProvider.get(jsonObject.typInformation);
            this.listOfGenerators.push(generator);
            generator.setJSON(jsonObject);
            var dataNode = generator.createStub();
            var newID = this.iDManager.getNewID();
            this._iDMapper.set(jsonObject.dataNodeId, newID);
            dataNode.setDataNodeId(newID);
            this.iDManager.set(newID, dataNode);
        };
        Object.defineProperty(JSON_To_DataNodes.prototype, "iDMapper", {
            get: function () {
                return this._iDMapper;
            },
            enumerable: true,
            configurable: true
        });
        return JSON_To_DataNodes;
    }());
    exports.JSON_To_DataNodes = JSON_To_DataNodes;
});
define("model/NodeWithLinkText", ["require", "exports", "model/observe", "model/HasDetail", "model/IDManager", "model/TextObject"], function (require, exports, observe_6, HasDetail_6, IDManager_10, TextObject_2) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO Caution: copy of old SimpleDataNode
    var SimpleDataNode = (function (_super) {
        __extends(SimpleDataNode, _super);
        function SimpleDataNode(name) {
            var _this = _super.call(this) || this;
            _this.name = [];
            _this.relationships = [];
            _this.name = name;
            return _this;
        }
        SimpleDataNode.createStubFromJSON = function (jsonDataNode) {
            var dataNode = new SimpleDataNode([new TextObject_2.TextObject(jsonDataNode["name"])]);
            IDManager_10.IDManager.singleton.setIdForDataNode(dataNode, jsonDataNode["dataNodeId"]);
            return dataNode;
        };
        SimpleDataNode.completeStub = function (stub, jsonDataNode) {
            var relationshipsJSON = jsonDataNode["relationships"];
            for (var i = 0; i < relationshipsJSON.length; i++) {
                var currentID = relationshipsJSON[i];
                var currentRelationship = IDManager_10.IDManager.singleton.getDataNodeForId(currentID);
                stub.relationships[i] = currentRelationship;
                stub.configureRelationship(currentRelationship);
            }
        };
        SimpleDataNode.createInstance = function (name) {
            var instance = new SimpleDataNode(name);
            IDManager_10.IDManager.singleton.takeDataNode(instance);
            return instance;
        };
        SimpleDataNode.createHasDetailAndSetConnector = function (from, to) {
            var rel = HasDetail_6.HasDetail.createInstance(from, to);
            from.addRelationship(rel);
        };
        SimpleDataNode.prototype.setDataNodeId = function (id) {
            this.dataNodeId = id;
        };
        SimpleDataNode.prototype.getDataNodeId = function () {
            return this.dataNodeId;
        };
        SimpleDataNode.prototype.configureRelationship = function (relationship) {
            var self = this;
            relationship.onDelete(function () {
                self.deleteRelationship(relationship);
            });
        };
        SimpleDataNode.prototype.deleteRelationship = function (relationship) {
            var index = this.relationships.indexOf(relationship);
            this.relationships.splice(index, 1);
            this.notify(observe_6.ObActions.RemovedRelationship, relationship, index);
        };
        SimpleDataNode.prototype.getObjectAsJSON = function () {
            var jsonObject = {};
            jsonObject["dataNodeId"] = this.dataNodeId;
            jsonObject["name"] = this.name[0].text;
            jsonObject["classAttr"] = "SimpleDataNode";
            var jsonRelationshipsList = [];
            for (var i = 0; i < this.relationships.length; i++) {
                jsonRelationshipsList[i] = this.relationships[i].getDataNodeId();
            }
            jsonObject["relationships"] = jsonRelationshipsList;
            return jsonObject;
        };
        SimpleDataNode.prototype.getName = function () {
            return this.name;
        };
        SimpleDataNode.prototype.setName = function (name) {
            this.name = name;
            this.notify(observe_6.ObActions.ChangedName, null, null);
        };
        SimpleDataNode.prototype.addRelationshipAtPosition = function (toAdd, position) {
            this.relationships.splice(position, 0, toAdd);
            this.configureRelationship(toAdd);
            this.notify(observe_6.ObActions.AddedRelationship, toAdd, position);
        };
        SimpleDataNode.prototype.addRelationship = function (relationship) {
            this.relationships.push(relationship);
            this.configureRelationship(relationship);
            this.notify(observe_6.ObActions.AddedRelationship, relationship, this.relationships.length - 1);
        };
        SimpleDataNode.prototype.getRelationships = function () {
            return this.relationships;
        };
        SimpleDataNode.prototype.getType = function () {
            // not used here
        };
        return SimpleDataNode;
    }(observe_6.Observable));
    exports.SimpleDataNode = SimpleDataNode;
});
define("model/SimpleDataNode_New", ["require", "exports", "general/observe/ObservableList", "general/observe/ObservableString", "model/A_DataNode"], function (require, exports, ObservableList_1, ObservableString_1, A_DataNode_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO replaced by Text_Connetors !!!
    var SimpleDataNode_New = (function (_super) {
        __extends(SimpleDataNode_New, _super);
        function SimpleDataNode_New() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            _this._dataNodeList = new ObservableList_1.ObservableList();
            _this._text = new ObservableString_1.Observable_String_Data();
            return _this;
        }
        SimpleDataNode_New.prototype.getObjectAsJSON = function () {
            throw new Error("Method not implemented.");
        };
        SimpleDataNode_New.prototype.getDependencies = function () {
            throw new Error("Method not implemented.");
        };
        Object.defineProperty(SimpleDataNode_New.prototype, "dataNodeList", {
            get: function () {
                return this._dataNodeList;
            },
            set: function (value) {
                this._dataNodeList = value;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(SimpleDataNode_New.prototype, "text", {
            get: function () {
                return this._text;
            },
            set: function (value) {
                this._text = value;
            },
            enumerable: true,
            configurable: true
        });
        return SimpleDataNode_New;
    }(A_DataNode_1.A_DataNode));
    exports.SimpleDataNode_New = SimpleDataNode_New;
});
define("model/Text_Connectors", ["require", "exports", "general/observe/ObservableList", "general/observe/ObservableString", "model/A_DataNode"], function (require, exports, ObservableList_2, ObservableString_2, A_DataNode_2) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var Text_Connectors = (function (_super) {
        __extends(Text_Connectors, _super);
        function Text_Connectors() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            _this._dataNodeList = new ObservableList_2.ObservableList();
            _this._text = new ObservableString_2.Observable_String_Data();
            return _this;
        }
        Text_Connectors.prototype.getObjectAsJSON = function () {
            throw new Error("Method not implemented.");
        };
        Text_Connectors.prototype.getDependencies = function () {
            throw new Error("Method not implemented.");
        };
        Object.defineProperty(Text_Connectors.prototype, "dataNodeList", {
            get: function () {
                return this._dataNodeList;
            },
            set: function (value) {
                this._dataNodeList = value;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(Text_Connectors.prototype, "text", {
            get: function () {
                return this._text;
            },
            set: function (value) {
                this._text = value;
            },
            enumerable: true,
            configurable: true
        });
        return Text_Connectors;
    }(A_DataNode_2.A_DataNode));
    exports.Text_Connectors = Text_Connectors;
});
define("Tester/Tester", ["require", "exports", "general/DisplayLogger"], function (require, exports, DisplayLogger_1) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var Tester = (function () {
        function Tester() {
            var displayLogger = new DisplayLogger_1.DisplayLogger();
            document.body.appendChild(displayLogger.getUIObject());
            this.logger = displayLogger;
        }
        Tester.run = function () {
            new Tester().runTests();
        };
        Tester.prototype.runTests = function () {
            this.logger.log("test");
        };
        return Tester;
    }());
    exports.Tester = Tester;
});
define("visual/ListRepresentation", ["require", "exports", "general/List"], function (require, exports, List_4) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var ListRepresentation = (function () {
        function ListRepresentation(listElements) {
            this.subVisualNodes = new List_4.List();
            this.myDiv = Utils.getDiv();
            for (var i = 0; i < listElements.getLength(); i++) {
                this.insertVisualNodeAtPosition(listElements[i], i);
            }
        }
        ListRepresentation.prototype.insertVisualNodeAtPosition = function (visualNode, position) {
            var visualNodeDiv = visualNode.getUIObject();
            if (position == this.subVisualNodes.getLength()) {
                this.myDiv.appendChild(visualNodeDiv);
            }
            else {
                // it is possible that myDiv.children.length > subVisualNodes.getLength()
                var UIObject_After = this.subVisualNodes.get(position).getUIObject();
                this.myDiv.insertBefore(visualNodeDiv, UIObject_After);
            }
            this.subVisualNodes.insert(visualNode, position);
        };
        ListRepresentation.prototype.removeVisualNodeAtPosition = function (position) {
            this.subVisualNodes.get(position).removeFromDOM();
            this.subVisualNodes.remove(position);
        };
        ListRepresentation.prototype.getUIObject = function () {
            return this.myDiv;
        };
        ListRepresentation.prototype.getVisualNodeAtPosition = function (position) {
            return this.subVisualNodes.get(position);
        };
        return ListRepresentation;
    }());
    exports.ListRepresentation = ListRepresentation;
});
define("visual/SimpleHeadBody", ["require", "exports", "./AbstractVisualHeadBody", "visual/ListController"], function (require, exports, AbstractVisualHeadBody_1, ListController_2) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO delete
    var SimpleHeadBody = (function (_super) {
        __extends(SimpleHeadBody, _super);
        function SimpleHeadBody() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        SimpleHeadBody.prototype.createBody = function (maxWidth) {
            this.createRelationshipController(maxWidth);
        };
        SimpleHeadBody.prototype.createRelationshipController = function (maxWidth) {
            var relationships = [];
            for (var i = 0; i < this.simpleVisualNode.getDataNode().getRelationships().length; i++) {
                var currentRelationship = this.dataNode.getRelationships()[i];
                var visualRelationship = this.simpleVisualNode.getVisualNodeForDataNode(currentRelationship);
                relationships[i] = visualRelationship;
            }
            this.relationshipsController = new ListController_2.ListController(relationships, maxWidth);
            this.configureRelationshipsController();
        };
        SimpleHeadBody.prototype.configureTextField = function () {
            var self = this;
            this.simpleHeadBody.getHead().onTextChange(function () {
                // update simpleDataNode
                self.textFieldChanged();
            });
        };
        SimpleHeadBody.prototype.configureRelationshipsController = function () {
            var self = this;
            this.relationshipsController.onChildLeavesWithEnter(function (listElem) {
                self.simpleVisualNode.relationshipsController_childLeavesWithEnter(listElem);
            });
        };
        SimpleHeadBody.prototype.getBody = function () {
            return this.relationshipsController;
        };
        SimpleHeadBody.prototype.getHead = function () {
            return this.simpleVisualNode.getHead();
        };
        SimpleHeadBody.prototype.bodyAvailable = function () {
            return this.dataNode.getRelationships().length > 0;
        };
        SimpleHeadBody.prototype.getEventManager = function () {
            return this.simpleVisualNode.getEventManager();
        };
        SimpleHeadBody.prototype.getBackgroundColor = function () {
            return this.simpleVisualNode.getBackgroundColor();
        };
        return SimpleHeadBody;
    }(AbstractVisualHeadBody_1.AbstractVisualHeadBody));
    exports.SimpleHeadBody = SimpleHeadBody;
});
define("visual/VisualTextObject", ["require", "exports", "visual/Interfaces/interfaces", "visual/Callbacks", "visual/ColorManagement", "visual/Utils"], function (require, exports, interfaces_1, Callbacks_5, ColorManagement_8, Utils_7) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO not used at the moment
    var VisualTextObject = (function (_super) {
        __extends(VisualTextObject, _super);
        function VisualTextObject(textObject, backgroundColor) {
            var _this = _super.call(this) || this;
            _this._myDiv = null;
            _this._textObject = textObject;
            _this.backgroundColor = backgroundColor;
            return _this;
        }
        VisualTextObject.prototype.getUIObject = function () {
            this._mySpan = document.createElement("span");
            this._mySpan.innerHTML = this._textObject.text;
            this._mySpan.visualNode = this;
            this._mySpan.contentEditable = true;
            this._mySpan.className = "pointer";
            var self = this;
            this._mySpan.onclick = function (ev) {
                if (ev.ctrlKey) {
                    self.totalZoomEvent();
                }
                else {
                    self.toggleEvent();
                }
                self.focusEvent();
            };
            this._mySpan.oncontextmenu = function (ev) {
                // console.log(ev.ctrlKey);
                if (ev.ctrlKey) {
                    self.zoomOutEvent();
                }
                else {
                    self.zoomInEvent();
                }
                ev.preventDefault();
                self.focusEvent();
            };
            if (this._textObject.isLink) {
                this._mySpan.className = "seli";
            }
            return this._mySpan;
        };
        VisualTextObject.prototype.totalZoomEvent = function () {
            if (this._textObject.isLink) {
                console.log('not implemented yet (is a link)');
            }
            else {
                this.onTotalZoomEventAttr.call(this);
            }
        };
        VisualTextObject.prototype.zoomInPossible = function () {
            return undefined;
        };
        VisualTextObject.prototype.zoomOutPossible = function () {
            return undefined;
        };
        VisualTextObject.prototype.toggleEvent = function () {
            if (this._textObject.isLink) {
                this.toggle();
            }
            else {
                this.onToggleZoomAttr.call(this);
            }
        };
        VisualTextObject.prototype.toggle = function () {
            if (this._myDiv == null) {
                this.zoomIn();
            }
            else {
                Utils_7.Utils.remove(this._myDiv);
                this._myDiv = null;
            }
        };
        VisualTextObject.prototype.zoomIn = function () {
            if (this._myDiv == null) {
                var visualNode = interfaces_1.getStandardVisualNodeForDataNode(this._textObject.linksTo, ColorManagement_8.getColorForChild(this.backgroundColor), this);
                this._myDiv = document.createElement("div");
                this._myDiv.style.marginLeft = (interfaces_1.MARGIN_LEFT_BODY + interfaces_1.PADING_NODE) + "px";
                this._myDiv.style.marginRight = (interfaces_1.MARGIN_RIGHT_BODY + interfaces_1.PADING_NODE) + "px";
                this._myDiv.style.marginBottom = "3" + "px";
                this._myDiv.style.marginTop = "3" + "px";
                this._myDiv.appendChild(visualNode.getUIObject());
                Utils_7.Utils.insertAfter(this._mySpan, this._myDiv);
                visualNode.zoomIn();
            }
            else {
            }
        };
        VisualTextObject.prototype.zoomOut = function () {
        };
        VisualTextObject.prototype.takeCursorFromBottom = function () {
        };
        VisualTextObject.prototype.takeCursorFromTop = function () {
        };
        VisualTextObject.prototype.getDataNode = function () {
            return undefined;
        };
        VisualTextObject.prototype.focus = function () {
        };
        VisualTextObject.prototype.removeFocus = function () {
        };
        return VisualTextObject;
    }(Callbacks_5.Callbacks));
    exports.VisualTextObject = VisualTextObject;
});
define("visual/TextWithLinks", ["require", "exports", "visual/Callbacks", "visual/Interfaces/interfaces", "model/TextObject", "visual/VisualTextObject", "visual/ColorManagement"], function (require, exports, Callbacks_6, interfaces_2, TextObject_3, VisualTextObject_1, ColorManagement_9) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // TODO: not used at the moment
    var TextWithLinks = (function (_super) {
        __extends(TextWithLinks, _super);
        function TextWithLinks(text, backgroundColor) {
            var _this = _super.call(this) || this;
            _this._text = text;
            _this.backgroundColor = backgroundColor;
            _this._visualTextObjects = [];
            var self = _this;
            for (var i = 0; i < text.length; i++) {
                _this._visualTextObjects[i] = new VisualTextObject_1.VisualTextObject(text[i], _this.backgroundColor);
                _this._visualTextObjects[i].onToggleZoomEvent(function () {
                    self.toggleEvent();
                });
                _this._visualTextObjects[i].onTotalZoomEvent(function () {
                    self.totalZoomEvent();
                });
                _this._visualTextObjects[i].onZoomInEvent(function () {
                    self.zoomInEvent();
                });
                _this._visualTextObjects[i].onZoomOutEvent(function () {
                    self.zoomOutEvent();
                });
                _this._visualTextObjects[i].onFocusEvent(function () {
                    self.focusEvent();
                });
            }
            return _this;
        }
        TextWithLinks.prototype.getUIObject = function () {
            this.myDiv = document.createElement("div");
            this.myDiv.style.font = interfaces_2.FONT_SIZE + " " + interfaces_2.FONT;
            this.myDiv.style.color = ColorManagement_9.getColorValue(this.fontColor);
            for (var i = 0; i < this._visualTextObjects.length; i++) {
                this.myDiv.appendChild(this._visualTextObjects[i].getUIObject());
            }
            return this.myDiv;
        };
        TextWithLinks.prototype.setFontColor = function (color) {
            this.fontColor = color;
        };
        TextWithLinks.prototype.zoomInPossible = function () {
            return undefined;
        };
        TextWithLinks.prototype.zoomOutPossible = function () {
            return undefined;
        };
        TextWithLinks.prototype.zoomIn = function () {
        };
        TextWithLinks.prototype.zoomOut = function () {
        };
        TextWithLinks.prototype.takeCursorFromBottom = function () {
            this._visualTextObjects[0].focus();
        };
        TextWithLinks.prototype.takeCursorFromTop = function () {
            this._visualTextObjects[0].focus();
        };
        TextWithLinks.prototype.getDataNode = function () {
            return undefined;
        };
        TextWithLinks.prototype.focus = function () {
        };
        TextWithLinks.prototype.removeFocus = function () {
        };
        TextWithLinks.createTextWithoutLinks = function (text, backgroundColor) {
            return new TextWithLinks([new TextObject_3.TextObject(text)], backgroundColor);
        };
        return TextWithLinks;
    }(Callbacks_6.Callbacks));
    exports.TextWithLinks = TextWithLinks;
});
</script>
</body>
</html>
'''