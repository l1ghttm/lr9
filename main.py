from collision import first,second,third,fourth
first.isCorrectRect()
second.isCollisionRect()
third.intersectionAreaRect()

rectangles = [
    [(-5, 4), (3, 7)],
    [(-3, 0), (10, 12)],
    [(0, 1), (5, 5)],
    [(2, 2), (7, 4)]
]
fourth.intersectionAreaMultiRect(rectangles)
