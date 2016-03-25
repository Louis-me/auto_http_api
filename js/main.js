/**
 * Created by Administrator on 2016/1/6.
 */
function getXML() {
    $.ajax({
        url: 'xml/main.xml',
        type: 'GET',
        dataType: 'xml',//这里可以不写，但千万别写text或者html!!!
        timeout: 1000,
        error: function (xml) {
            alert('Error loading XML document' + xml);
        },
        success: function (xml) {
            $(xml).find("root").each(function (i) {
                console.log($(this).find("title").text());
                l = $(this).find("InterfaceList");
                l.each(function(index,value){
                    console.log($(this).find("name").text());
                    console.log($(this).find("method").text());
                    //console.log(value);
                });
            });
        }
    });
}

function setXML(){
    $.ajax({
        url: 'xml/main_add.xml',
        type: 'GET',
        dataType: 'xml',//这里可以不写，但千万别写text或者html!!!
        timeout: 1000,
        error: function (xml) {
            alert('Error loading XML document' + xml);
        },
        success: function (xml) {
            $(xml).find("root").each(function (i) {
                $(this).append("<title>接口测试</title>")
                console.log($(this))
            });
        }
    });

}