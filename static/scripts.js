get_last_part_of_path = function() {
    // https://example.com/foo/bar/spam?haha=true -> spam
    return document.URL.split('/').pop().split('?')[0]
}

send_get_request = function(url, func_success, func_error) {
    var xmlhttp = new XMLHttpRequest();
    var json;
    xmlhttp.open('GET', url, true);
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            func_success(JSON.parse(xmlhttp.responseText));
        }
        else {
            func_error(xmlhttp.status);
        }
    };
    xmlhttp.send(null);
}

lesson_html = function(obj) {
    return `<li class="lesson"> \
<div class="name">${obj.name}</div> \
<div class="time">${obj.start.slice(0,5)}-${obj.end.slice(0,5)}</div> \
<div class="room">${obj.room}</div> \
<div class="address">${obj.address}</div> \
<div class="group">${obj.group}</div> \
</li>`
}

list_injector = function(method_url) {
    url = method_url + get_last_part_of_path();
    proc = function(json) {
        list = document.getElementById('lessons-list');
        injection = "";
        json.forEach(function(item, i) {
            injection += lesson_html(item);
        })
        list.innerHTML = injection;
    };
    status_proc = function(status) {
        console.log(status)
    };
    send_get_request(url, proc, status_proc);
}