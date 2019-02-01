const value_parse = /\$*[A-Z]+[0-9]+/g;
const sub_parse = /[0-9]+\.[0-9]+-[0-9]+\.[0-9]+/g;
const plus_parse = /[0-9]+\.[0-9]+\+[0-9]+\.[0-9]+/g;
const less_parse = /[0-9]+\.[0-9]+<[0-9]+\.[0-9]+/g;
const greater_parse = /[0-9]+\.[0-9]+>[0-9]+\.[0-9]+/g;
const and_parse = /AND\((.*?)\)/g;
const if_parse = /=IF\((.*)\)/g;

function replace_value(result, test1) {
    for(var value in result){
        var num = values[result[value]];
        test1 = test1.replace(result[value], String(num));
    }
    return test1;
}

function sub_calc(result) {
    var calcs = result.match(sub_parse);
    if(calcs != null)
    {
        for(var i in calcs){
            calc = calcs[i];
            var result2 = calc.split('-');
            var a = Number(result2[0]);
            var b = Number(result2[1]);
            var num = a - b;
            result = result.replace(calc, String(num));
        }
    }
    return result;
}

function plus_calc(result) {
    var calcs = result.match(plus_parse);
    if(calcs != null)
    {
        for(var i in calcs){
            calc = calcs[i];
            var result2 = calc.split('+');
            var a = Number(result2[0]);
            var b = Number(result2[1]);
            var num = a + b;
            result = result.replace(calc, String(num));            
        }
    }
    return result;
}

function less_calc(result) {
    var calcs = result.match(less_parse);
    if(calcs != null)
    {
        for(var i in calcs){
            calc = calcs[i];
            var result2 = calc.split('<');
            var a = Number(result2[0]);
            var b = Number(result2[1]);
            if(a < b){
                result = result.replace(calc, "True");
            }else{
                result = result.replace(calc, "False");
            }
        }
    }
    return result;
}

function greater_calc(result) {
    var calcs = result.match(greater_parse);
    if(calcs != null)
    {
        for(var i in calcs){
            calc = calcs[i];
            var result2 = calc.split('>');
            var a = Number(result2[0]);
            var b = Number(result2[1]);
            if(a > b){
                result = result.replace(calc, "True");
            }else{
                result = result.replace(calc, "False");
            }
        }
    }
    return result;
}

function and_calc(result) {
    var calcs = result.match(and_parse);
    if(calcs != null)
    {
        for(var i in calcs){
            calc = calcs[i];
            var match = and_parse.exec(result)[1];
            var result2 = match.split(',')
            if(result2[0] == "True" && result2[1] == "True"){
                result = result.replace(calc, "True");
            }else{
                result = result.replace(calc, "False");
            }
        }
    }
    return result
}

function if_calc(result) {
    var match = if_parse.exec(result)[1];
    if(match)
    {
        var result2 = match.split(',')
        if(result2[0] == "True"){
            return result2[1];
        }else{
            return result2[2];
        }      
    }
    return null;
}

var test1 = '=IF(AND(A16-$A11<Z11,A16+$A12>Z12), "OK", "FALSE")';
var A16 = 88.001;
var A11 = 0.015;
var A12 = 0.003;
var Z11 = 87.996;
var Z12 = 88.006;
var values = { "A16":A16, "$A11":A11, "$A12":A12, "Z11":Z11, "Z12":Z12 };

function calc_run(test1) {
    var result = test1.match(value_parse);
    result = replace_value(result, test1);
    result = sub_calc(result);
    result = plus_calc(result);
    result = less_calc(result);
    result = greater_calc(result);
    result = and_calc(result);
    result = if_calc(result);
    return result;
}

var result = calc_run(test1);
console.log(test1 + " : " + result);