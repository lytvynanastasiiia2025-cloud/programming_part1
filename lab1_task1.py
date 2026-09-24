a_length = int(input("enter the length: "))
b_width = int(input("enter the width: "))
c_height = int(input("enter the height: "))

volume_parallelepiped = a_length*b_width*c_height;
area_parallelepiped = 2*(a_length*b_width + b_width*c_height + a_length*c_height); 
print("volume_parallelepiped =", volume_parallelepiped);
print("area_parallelepiped =", area_parallelepiped);
