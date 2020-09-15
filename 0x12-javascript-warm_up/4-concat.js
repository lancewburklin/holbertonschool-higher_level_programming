#!/usr/bin/node
if (typeof(process.argv[2]) === 'undefined'){
  const par1 = 'undefined';
  console.log('undefined is undefined');
} else {
  const par1 = process.argv[2];
  if (typeof(process.argv[3]) === 'undefined'){
  console.log(par1 + ' is undefined');
} else {
  console.log(par1 + ' is ' + process.argv[3]);
}
}
