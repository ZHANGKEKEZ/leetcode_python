/*
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/simplify-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths=path.split('/')
        res=[]
        for path in paths:
            if path=='..' and res:
                res.pop()
            #这里的不等于空很关键，遇到//时，split是把两个/之间当作""存储的
            if path!='.'and path!='..'and path!='':
                res.append(path)
        #注意字符串join函数的用法
        r="/"+"/".join(res)
        return r
