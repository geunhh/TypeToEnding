export function applyStyles() {



    const elements = document.querySelectorAll('div');
    elements.forEach(element => {
        element.style.border = '2px solid gray'; // 예시 스타일
        element.style.backgroundColor = 'white';
    });

    elements.forEach(element => {
        // 스타일 클래스 추가
        element.classList.add('btn-primary'); // styleguide.css의 클래스 추가
        element.classList.add('text-large');  // 추가적인 스타일 클래스
    });

    // 다른 태그에 대해서도 동일하게 적용할 수 있습니다.
    const buttons = document.querySelectorAll('.afterlogin-btn');
    buttons.forEach(button => {
        button.classList.add('btn-primary'); // 버튼에 스타일 추가
    });




}