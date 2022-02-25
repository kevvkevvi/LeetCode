class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # map each course to their prerequisites
        prereq = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        # set to represent visited nodes in dfs
        visited = set()
        def dfs(i):
            # we have a loop --> impossible to complete all courses
            if i in visited:
                return False
            # if we end up having an empty list for a course, it's
            # true because the prerequisites are satisfied
            if not prereq[i]:
                return True
            visited.add(i)
            # check all prerequisites of this course
            for pre in prereq[i]:
                # call dfs on that prereq, if any create
                # a loop, return false
                if not dfs(pre):
                    return False
                # remove that prereq from the prerequisite list
                prereq[i].remove(pre)
            # we're done with this course, so remove from visited
            visited.remove(i)
            return True
        # call dfs on all courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True