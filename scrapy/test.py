from sklearn.ensemble import RandomForestClassifier
import osgeo
from osgeo import gdal
from osgeo import osr
from osgeo import ogr


def GetSubRaster(inraster, polygonPoints: list):
    polygonPoints.append(polygonPoints[0])  # 面多边形坐标封闭
    print("当前多边形节点数量：" + str(len(polygonPoints)))
    # 计算最小边界矩形
    minX = 10000000000000
    maxX = -minX
    minY = 100000000000000000
    maxY = -minY

    for point in polygonPoints:
        if point.X < minX: minX = point.X
        if point.X > maxX: maxX = point.X
        if point.Y < minY: minY = point.Y
        if point.Y > maxY: maxY = point.Y
    leftX = minX
    upY = maxY
    rightX = maxX
    bottomY = minY

    rds = gdal.Open(inraster)
    transform = (rds.GetGeoTransform())
    lX = transform[0]  # 左上角点
    lY = transform[3]
    rX = transform[1]  # 分辨率
    rY = transform[5]

    wpos = int((leftX - lX) / rX)
    hpos = int((upY - lY) / rY)

    width = int((rightX - leftX) / rX)
    height = int((bottomY - upY) / rY)
    BandsCount = rds.RasterCount
    arr = rds.ReadAsArray(wpos, hpos, width, height)
    fixX = list()
    nodatavalue = rds.GetRasterBand(1).GetNoDataValue()
    for i in range(height):
        if height > 200:
            print(f"多边形裁剪进度：{round(((i + 1) / height) * 100, 4)}%")
        Y = upY + i * rY + .00001
        # 射线算法只需要比对多边形的一条水平线上的边
        pointsindex = list()
        for k in range(len(polygonPoints) - 1):
            point1 = polygonPoints[k]
            point2 = polygonPoints[k + 1]
            if (point1.Y >= Y and point2.Y <= Y) or (point1.Y <= Y and point2.Y >= Y):
                pointsindex.append(k)
        for j in range(width):
            count = 0
            for m in (pointsindex):
                point1 = polygonPoints[m]
                point2 = polygonPoints[m + 1]
                X = leftX + j * rX + .00001
                if point1.X == point2.X:
                    intersectX = point1.X
                    if intersectX > X: count += 1
                else:
                    k = (point2.Y - point1.Y) / (point2.X - point1.X)
                    if k == 0:
                        if X < point1.X or X < point2.X:
                            count += 1
                    else:
                        intersectX = (Y - point1.Y) / k + point1.X
                        if intersectX > X: count += 1

            if count % 2 == 0:
                if BandsCount > 1:
                    for bc in range(BandsCount):
                        arr[bc][i][j] = (nodatavalue)
                else:
                    arr[i][j] = -1
    # 为了测试结果的正确性，可以先将其写到硬盘
    # WriteRaster("test.tif",arr,inraster,width,height,BandsCount,leftX,upY)
    return arr, width, height, BandsCount, leftX, upY
