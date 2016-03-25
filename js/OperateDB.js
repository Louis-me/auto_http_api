/**
 * Created by Administrator on 2016/1/7.
 */
function openDB (name,version) {
    var version=version || 1;
    var request=window.indexedDB.open(name,version);
    request.onerror=function(e){
        console.log(e.currentTarget.error.message);
    };
    request.onsuccess=function(e){
        result =e.target.result;
        console.log(result.name);

    };
    request.onupgradeneeded=function(e){
        console.log('DB version changed to '+version);
    };
}

