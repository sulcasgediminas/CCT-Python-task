import math

def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
    min_illumination = float('inf')
    darkest_index = -1
    replacements = 0

    for i in not_working_street_lights:
        illumination = 0

        # Calculate illumination from the neighboring working lights on the left
        for j in range(i-1, -1, -1):
            if j not in not_working_street_lights:
                distance = (i - j) * 20
                if distance / 100 > math.sqrt(-math.log(0.01, 3)):
                    break
                illumination += 3 ** (-(distance / 100) ** 2)

        # Calculate illumination from the neighboring working lights on the right
        for j in range(i+1, road_length // 20 + 1):
            if j not in not_working_street_lights:
                distance = (j - i) * 20
                if distance / 100 > math.sqrt(-math.log(0.01, 3)):
                    break
                illumination += 3 ** (-(distance / 100) ** 2)

        if illumination < min_illumination:
            min_illumination = illumination
            darkest_index = i

        if illumination < 1:
            replacements += 1

    return darkest_index, replacements


road_length = 2000
not_working_street_lights = [5,6,7,11,12,13,14,15,16,17,18,19,20,21,22]
darkest_index, replacements = find_index_of_darkest_street_light(road_length, not_working_street_lights)
print("Darkest Index:", darkest_index)
print("Minimal Replacements:", replacements)