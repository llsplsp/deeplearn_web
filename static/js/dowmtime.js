onload=function () {
        setInterval(go,1000)
    };

    var ms=1799;
    var m=ms%30;
    var s=ms%60;
    function go() {

        if (ms>=0){
            document.getElementById("spm").innerText=m+'分钟';
            document.getElementById("sps").innerText=s+'秒';
            ms--;
        }else {
            location.href="/day06/index";
        }
        if (s==0)
            m=m-1

    }