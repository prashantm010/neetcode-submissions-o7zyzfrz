import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        path = re.sub(r'/+', '/', path)
        paths = path.strip('/').split('/')
        for ele in paths:
            if ele == '' or ele == '.':
                continue
            elif ele == '..':
                if st:
                    st.pop()
            else:
                st.append(ele)
        return '/' + '/'.join(st)
        