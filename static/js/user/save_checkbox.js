// id_userLoginId
// id_password
// bxid_rememberMe_true
//
// 인터넷에서 범용적으로 돌고 있는 예제이다. 쿠키를 7일 동안 심거나 쿠키를 가져오거나 삭제한다.

$(document).ready(function(){

    // 저장된 쿠키값을 가져와서 ID 칸에 넣어준다. 없으면 공백으로 들어감.
    let key = getCookie("key");
    $("#id_userLoginId").val(key);

    if($("#id_userLoginId").val() != ""){ // 그 전에 ID를 저장해서 처음 페이지 로딩 시, 입력 칸에 저장된 ID가 표시된 상태라면,
        $("#bxid_rememberMe_true").attr("checked", true); // ID 저장하기를 체크 상태로 두기.
    }

    $("#bxid_rememberMe_true").change(function(){ // 체크박스에 변화가 있다면,
        if($("#bxid_rememberMe_true").is(":checked")){ // 체크박스 체크했을 때,
            setCookie("key", $("#id_userLoginId").val(), 7); // 7일 동안 쿠키 보관
        }else{ // ID 저장하기 체크 해제 시,
            deleteCookie("key");
        }
    });
    // ID 저장하기를 체크한 상태에서 ID를 입력하는 경우, 이럴 때도 쿠키 저장.
    $("#id_userLoginId").keyup(function(){ // ID 입력 칸에 ID를 입력할 때,
        if($("#bxid_rememberMe_true").is(":checked")){ // 체크박스를 체크한 상태라면,
            setCookie("key", $("#id_userLoginId").val(), 7); // 7일 동안 쿠키 보관
        }
    });
});

function setCookie(cookieName, value, exdays){
    let exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    let cookieValue = escape(value) + ((exdays==null) ? "" : "; expires=" + exdate.toGMTString());
    document.cookie = cookieName + "=" + cookieValue;
}
function deleteCookie(cookieName){
    let expireDate = new Date();
    expireDate.setDate(expireDate.getDate() - 1);
    document.cookie = cookieName + "= " + "; expires=" + expireDate.toGMTString();
}
function getCookie(cookieName) {
    cookieName = cookieName + '=';
    let cookieData = document.cookie;
    let start = cookieData.indexOf(cookieName);
    let cookieValue = '';
    if(start != -1){
        start += cookieName.length;
        let end = cookieData.indexOf(';', start);
        if(end == -1)end = cookieData.length;
        cookieValue = cookieData.substring(start, end);
    }
    return unescape(cookieValue);
}