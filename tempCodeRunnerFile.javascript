var palindromeChainLength = function(n, res = 0) {
  const str = n.toString()
  const revStr = n.toString().split('').reverse().join()
  if(str === revStr) {
    res += palindromeChainLength(n + parseInt(revStr, res)) + 1
    console.log(res)
  }
  return res
};

palindromeChainLength(87)