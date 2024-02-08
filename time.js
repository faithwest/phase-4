function generateNumberVariations(arr) {
    const variations = [];

for (const num of (arr)) {
    const numStr = num.toString();
    const numLength = numStr.length;
    const visited = Array(numLength).fill(false);

    


    function generatePermutations(currentIndex, currentNum) {
        if (currentIndex === numLength) {
            variations.push(currentNum);
            return;
        }

        for (let i = 0; i < numLength; i++) {
            if (!visited[i]) {
                visited[i] = true;
                generatePermutations(currentIndex + 1, currentNum * 10 + parseInt(numStr[i]));
                visited[i] = false;
            }
        }
    }

    generatePermutations(0, 0);
}

return variations;
}

function timeAmPm(num) {
    const variations = generateNumberVariations([num]);
    const results = [];

for (const variation of variations) {
    const variationStr = variation.toString();
    if (variationStr.length >= 4) {
        const part1 = variationStr.substring(0, 2);
        const part2 = variationStr.substring(2);

        if (parseInt(part1) <= 23 && parseInt(part2) <= 60) {
            let result = '';
                                

            if (parseInt(part1) >= 12 && part2 >= "00") {
                result = "pm";
            } else if (parseInt(part1) === 12 && part2 === "00") {
                result = "noon";
            } else {
                result = "am";
            }

            results.push({
                time: `${part1}:${part2}`,
                period: result
            });
        } else if ((parseInt(part1) === 24)&&(parseInt(part2) <=60)) {
            results.push({
                time: "00:" + part2,
                period: "am"
            });
        }
        //  else {
        //     return "invalid format";
        // }
    }

}

return results.length > 0 ? results : "invalid format";
}

const variations = timeAmPm(2332);
console.log(variations);