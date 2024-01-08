function UpToN(n){
    let total = 0;//n1
    for (let i =1; i<=n; i++){//n2,n3,n4
        total =total +1;//n5*n
    }
    //big O = N1+N2+N3+N4+(N5*N)+N6
    //BIG0=N+n+n+n(N*N)+N
    //BIGO=5N+N
    //N*2
    //10+4
    //N=10
    //100
 return total;//n6
}
//console.log(UpToN(10000));


//better
function multi5(n){
    let ans= n *5;//n1,n2
    return ans;//n3
}

//0*2=NESTED LOOPS,UNSORTED LIST
function multiTable(n, m) {
    let arr1 = []; 
  
    for (let i = 0; i < n; i++) {
      let arr2 = [];
  
      for (let j = 0; j < m; j++) { 
        arr1.push(`1 * ${i} * ${j} = ${i * j}`); 
  
      arr1.push(arr2);
    }
  
    return arr1;
  }
  
}