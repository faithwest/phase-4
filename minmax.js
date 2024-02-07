function minimum(arr) {
    var min_val = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] < min_val) {
            min_val = arr[i];
        }
    }
    return min_val;
}

var arr = [42, 890, 2, 612, 120];
console.log("Minimum:", minimum(arr));

function maximum(arr) {
    var max_val = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    }
    return max_val;
}

var arr = [128, 802, 2, 698, 10];
console.log("Maximum:", maximum(arr));

var negatives = function(arr) {
    var min_neg = null;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0 && (min_neg === null || arr[i] > min_neg)) {
            min_neg = arr[i];
        }
    }
    return min_neg;
};

var arr = [4, 8, -2, -6, -10];
console.log("Most Minimum Negatives:", negatives(arr)); // Output: -2


