class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c != "]":
                st.append(c)
            else:
                subs = ""
                while st[-1] != "[":
                    subs = st.pop() + subs
                st.pop()

                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                st.append(int(k) * subs)

        return "".join(st)
