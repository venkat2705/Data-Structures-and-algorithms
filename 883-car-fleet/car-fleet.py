class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        # Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        # cars = [[10,2],[8,4],[5,1],[3,3],[0,1]]
        # stack = [1,7,12]

        st = []
        for pos,spd in cars:
            time = (target-pos)/spd
            if st and time<=st[-1]:
                continue
            st.append(time)
        return len(st)


        