function generateNumberVariations(arr) {
    const variations = [];


    for (const num of arr) {
      const numStr = num.toString();
      const numLength = numStr.length;
      // console.log(length ${numLength})
      const visited = Array(numLength).fill(false);

  console.log(` visited ${visited}`)
  
  // Use recursion to generate all permutations of the digits
  function generatePermutations(currentIndex, currentNum) {
    if (currentIndex === numLength) {
      variations.push(currentNum);
      // console.log(`variation ${variations}`);
      return;
    }
  
    for (let i = 0; i < numLength; i++) {
      if (!visited[i]) {
        visited[i] = true;
        generatePermutations(currentIndex + 1, currentNum * 10 + parseInt(numStr[i]));
        // console.log(`current num${currentNum}`)
        visited[i] = false;
        // console.log(visited[i])
      }
    }
  }
  
  generatePermutations(0, 0);
  // function filterOut(numStr){
  //   let filtered = numStr

  // }
}
  
return variations;
  }

 const arr= [9041]
 const variations=generateNumberVariations(arr)
 console.log(variations)
