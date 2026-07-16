class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for s in tokens:
            if s == "+" or s == "-" or s == "*" or s == "/":
                y=int(st.pop())
                x=int(st.pop())
                match s:
                    case "+":
                        st.append(x+y)
                    case "-":
                        st.append(x-y)
                    case "*":
                        st.append(x*y)
                    case "/":
                        st.append(x/y)
            else:
                st.append(s)
        return int(st.pop())