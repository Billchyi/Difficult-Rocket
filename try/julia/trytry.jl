#=
trytry:
- Julia version: 1.7.2
- Author: shenjack
- Date: 2022-01-17
=#

println("Hello, world!")

# 输入字符，然后输出输入的字符

function run()

ABigFloat = BigFloat(1111111111111111111111111111111111111111.1111111) * BigFloat(11111123.5111)
ABigInt = BigInt(11111111111111111111111111111111111111111111111) * BigInt(111111235111)


println("$ABigInt \n$ABigFloat")
end
run()

"""
1234569279011111111111111111111111111111111111098765418321
1.2345692790111111417743419014825244111008694272e+46
"""
