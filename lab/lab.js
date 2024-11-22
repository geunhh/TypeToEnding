const exampleString = '[{"round": 0, "situation": "타키 모리타(모리 오스카 분)와 미츠하 히카리(타카하시 미츠하 분)는 서로의 몸이 바뀌는 경험을 하며, 시간의 흐름에 이상이 있음을 깨닫게 됩니다. 그들은 이 현상이 단순한 꿈이나 환상이 아니라, 실제로 시간과 공간을 초월한 현상임을 알게 됩니다. 타키와 미츠하는 시간의 균열을 바로잡기 위해 과거로 돌아가야 할지, 아니면 현재에서 해결책을 찾아야 할지 결정해야 합니다.", "user_action": null, "score": 0, "next_situation": "타키 모리타(모리 오스카 분)와 미츠하 히카리(타카하시 미츠하 분)는 서로의 몸이 바뀌는 경험을 하며, 시간의 흐름에 이상이 있음을 깨닫게 됩니다. 그들은 이 현상이 단순한 꿈이나 환상이 아니라, 실제로 시간과 공간을 초월한 현상임을 알게 됩니다. 타키와 미츠하는 시간의 균열을 바로잡기 위해 과거로 돌아가야 할지, 아니면 현재에서 해결책을 찾아야 할지 결정해야 합니다."}, {"round": 2, "situation": "타키 모리타(모리 오스카 분)와 미츠하 히카리(타카하시 미츠하 분)는 서로의 몸이 바뀌는 경험을 하며, 시간의 흐름에 이상이 있음을 깨닫게 됩니다. 그들은 이 현상이 단순한 꿈이나 환상이 아니라, 실제로 시간과 공간을 초월한 현상임을 알게 됩니다. 타키와 미츠하는 시간의 균열을 바로잡기 위해 과거로 돌아가야 할지, 아니면 현재에서 해결책을 찾아야 할지 결정해야 합니다.", "user_action": "ㅎㅎㅎㅎㅎㅎ", "score": 0, "evaluation": "부적절함", "reason": "이유: 유저의 행동은 영화의 주요 테마와 갈등을 무시하고, 감정적 연결과 운명적 만남을 무시하는 비현실적인 선택입니다. 두 주요 캐릭터의 성장과 연결을 무시하며, 이야기의 진행에 부합하지 않습니다.", "next_situation": "두 주인공이 시간의 균열을 바로잡기 위해 현재에서 해결책을 찾기로 결정했지만, 갈등은 더 복잡해집니다. 시간의 흐름이 더 이상 예측할 수 없게 되고, 두 사람의 연결은 더욱 깊어지면서 새로운 비밀과 위험이 드러납니다. 이제 두 사람은 현재에서 해결책을 찾기 위해 더 많은 협력과 희생이 필요하게 됩니다."}]';

function removeEscapeCharacters(inputString) {
    // 이스케이프 문자를 제거합니다.
    return inputString
        .replace(/\\r/g, '') // \r 제거
        .replace(/\\n/g, '') // \n 제거
        .replace(/\\"/g, '"'); // 이스케이프된 따옴표를 원래의 따옴표로 변환
}

function parseStringToObjectArray(inputString) {
    const objectsArray = [];
    let currentObject = '';
    let braceCount = 0; // 중괄호 개수 카운트
    
    for (let char of inputString) {
        if (char === '{') {
            if (braceCount === 0) {
                currentObject = '{'; // 새로운 객체 시작
            }
            braceCount++;
        } else if (char === '}') {
            braceCount--;
            currentObject += char;
            
            if (braceCount === 0) {
                // 객체가 완성되면 배열에 추가
                objectsArray.push(JSON.parse(currentObject)); // JSON.parse를 사용하여 객체로 변환
                currentObject = ''; // 현재 객체 초기화
            }
        } else if (braceCount > 0) {
            currentObject += char; // 현재 객체에 추가
        }
    }
    
    return objectsArray;
}
const cleanedString = removeEscapeCharacters(exampleString);
const parsedString = parseStringToObjectArray(cleanedString)

console.log(parsedString);
