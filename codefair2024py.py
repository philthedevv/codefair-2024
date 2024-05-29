def calc_water_squares(holesHeight):
    calculated_sq,left,Max_on_Left,Max_on_Right, right = 0, 0, 0, 0, len(holesHeight) - 1

    while True:
        if(left < right):
            if(holesHeight[left]< holesHeight[right]):
                if(holesHeight[left] > Max_on_Left):
                    Max_on_Left = holesHeight[left]
                else:
                    calculated_sq += Max_on_Left - holesHeight[left]
                left+=1
            else:
                if(holesHeight[right]>Max_on_Right):
                    Max_on_Right = holesHeight[right]

                else:
                    calculated_sq += Max_on_Right - holesHeight[right]

                right-=1
        else:
            break

    return calculated_sq


roadHeight = [5,2,3,4,1,1,3,5]
print(calc_water_squares(roadHeight))
