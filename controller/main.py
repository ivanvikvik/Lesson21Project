from model.point2d import Point2D


def main():
    # print(Point2D.just_do_it())
    # print(Point2D.just_do_it)
    # print(Point2D().just_do_it())
    # print(Point2D().just_do_it)

    # print(Point2D.sum(5, 6))
    # print(Point2D.sum)
    # print(Point2D().sum(5, 6))
    # print(Point2D().sum)

    point1 = Point2D()
    point2 = Point2D()
    point3 = Point2D()
    point4 = Point2D()

    print(Point2D.get_count())

    del point4

    print(Point2D.get_count())

    # print(point1.calculate_distance(point1))
    # print(point1.calculate_distance)
    # print(Point2D.calculate_distance)
    #
    # Point2D.calculate_distance(point1)
    # print(hex(id(point)))
    # print(hex(hash(point)))


if __name__ == "__main__":
    main()
