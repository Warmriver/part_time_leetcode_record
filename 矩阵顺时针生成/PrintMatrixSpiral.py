# 顺时针打印给定矩阵 

def spiralOrder(matrix):
        if not matrix or not matrix[0]:
            return []
        rs, cs = 0, 0
        re, ce = len(matrix)-1, len(matrix[0]) - 1
        ret = []
        while rs <= re and cs <= ce:
            i = cs
            while i <= ce:
                ret.append(matrix[rs][i])
                i += 1
            rs += 1
            i = rs
            while i <= re:
                ret.append(matrix[i][ce])
                i+=1
            ce -= 1   
            i = ce
            while re >= rs and i >= cs:
                ret.append(matrix[re][i])
                i -=1
            re -=1    
            i = re
            while ce >= cs and i >= rs:
                ret.append(matrix[i][cs])
                i -=1
            cs += 1    
        return ret    

if __name__ == '__main__':
    ret = spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(ret)