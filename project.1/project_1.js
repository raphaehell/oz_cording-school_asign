const form = document.getElementById("form");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    let userId = event.target.id.value;
    let userPw1 = event.target.pw1.value;
    let userPw2 = event.target.pw2.value;
    let userName = event.target.name.value;
    let userPhone = event.target.phone.value;
    let userGender = event.target.gender.value;
    let userEmail = event.target.email.value;
    let userIntro = event.target.intro.value;

    if (userId.length < 6) {
        alert("아이디가 너무 짧습니다. 6자 이상으로 입력해주세요.");
        return;
    }

    if (userPw1 !== userPw2) {
        alert("입력하신 비밀번호가 일치하지 않습니다. 다시 한번 확인해주세요.");
        return;
    }

    alert(`${userName}님 회원가입이 완료되었습니다.`);

    // Admin 페이지로 이동
    window.location.href = "admin.html";
});