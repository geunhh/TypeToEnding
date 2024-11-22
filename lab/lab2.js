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
                objectsArray.push(parseObject(currentObject)); // 직접 구현한 함수로 객체 변환
                currentObject = ''; // 현재 객체 초기화
            }
        } else if (braceCount > 0) {
            currentObject += char; // 현재 객체에 추가
        }
    }
    
    return objectsArray;
}

// 객체 문자열을 파싱하여 객체로 변환
function parseObject(objectString) {
    const obj = {};
    const properties = objectString.slice(1, -1).split(','); // 중괄호 제거 후 각 속성으로 나누기

    for (let property of properties) {
        const [key, value] = property.split(':').map(item => item.trim()); // 키와 값으로 나누기
        const cleanedKey = key.replace(/"/g, ''); // 따옴표 제거
        const cleanedValue = parseValue(value); // 값 파싱
        obj[cleanedKey] = cleanedValue;
    }

    return obj;
}

// 값에 대한 파싱 처리
function parseValue(value) {
    if (value === 'null') {
        return null; // null 처리
    } else if (/^".*"$/.test(value)) {
        return value.replace(/"/g, ''); // 문자열 처리
    } else if (!isNaN(value)) {
        return Number(value); // 숫자 처리
    } else {
        return value; // 그 외 값 그대로 반환
    }
}

// 사용 예시
const exampleString = '[{"round": 0, "situation": "타키 모리타(모리 오스카 분)와 미츠하 히카리(타카하시 미츠하 분)는 서로의 몸이 바뀌는 경험을 하며, 시간의 흐름에 이상이 있음을 깨닫게 됩니다.", "user_action": null, "score": 0, "next_situation": "타키와 미츠하는 시간의 균열을 바로잡기 위해 과거로 돌아가야 할지, 아니면 현재에서 해결책을 찾아야 할지 결정해야 합니다."}, {"round": 2, "situation": "타키와 미츠하가 서로의 몸이 바뀌는 경험을 하며, 시간의 흐름에 이상이 있음을 깨닫게 됩니다.", "user_action": "ㅎㅎㅎㅎㅎㅎ", "score": 0, "evaluation": "부적절함", "reason": "이유: 유저의 행동은 영화의 주요 테마와 갈등을 무시하고, 감정적 연결과 운명적 만남을 무시하는 비현실적인 선택입니다.", "next_situation": "두 주인공이 시간의 균열을 바로잡기 위해 현재에서 해결책을 찾기로 결정했지만, 갈등은 더 복잡해집니다."}]';

const result = parseStringToObjectArray(exampleString);
console.log(result);
