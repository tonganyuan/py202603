def buildCar(*tools):
    print(tools)
    msg = "需要用到的工具有："
    for tool in tools:
        msg += f"-{tool}"
    print(msg)

buildCar("dadao")
buildCar("dadao","fuzi","daozi")