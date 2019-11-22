function sliceAndDice(arr1, arr2, index) {
    var arr3 = arr2.splice(index);
    var arr4 = arr2.concat(arr1);
    var arr5 = arr4.concat(arr3);
    return arr5;
}