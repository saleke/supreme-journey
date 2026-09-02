import sys 
# import antigravity

def get_geohash(latitude, longitude, precision):

    longitude_range = [-180.0, 180.0]
    latitude_range = [-90.0, 90.0]

    BASE32_ALPHABETS = "0123456789bcdefghjkmnpqrstuvwxyz"

    geohash = []
    bit_buffer = 0
    char_count = 0

    is_even_bit = True
    bits_needed = 5 * precision

    for _ in range(bits_needed):
        if is_even_bit:

            mid = (longitude_range[0] + longitude_range[1]) / 2
            if longitude >= mid:
                bit_buffer = (bit_buffer << 1) | 1
                longitude_range[0] = mid

            else:
                bit_buffer = (bit_buffer << 1) | 0
                longitude_range[1] = mid
        else:

            mid = (latitude_range[0] + latitude_range[1]) / 2
            if latitude >= mid:
                bit_buffer = (bit_buffer << 1) | 1
                latitude_range[0] = mid

            else:
                bit_buffer = (bit_buffer << 1) | 0
                latitude_range[1] = mid

        char_count += 1
        is_even_bit = not is_even_bit

        if char_count == 5:
            geohash.append(BASE32_ALPHABETS[bit_buffer])
            char_count = 0
            bit_buffer = 0

    return "".join(geohash)



def main():
    args = sys.argv[1:]

    if len(args) < 3 :
        print("Error: Missing parameters.")
        print("Usage: python geohashing.py <latitude> <longitude> [precision]")
        sys.exit(1)
    
    precision = 5

    try:
        latitude = float(args[0])
        longitude = float(args[1])
        precision = int(args[2])

    except ValueError:
        print("Error: Latitude and Longitude must be numbers. Precision must be an integer.")
        sys.exit(1)
    
    if longitude < -180 or longitude > 180:
        print(f"Error: Latitude ({longitude}) out of bounds. Must be between -180 and 180.")
        sys.exit(1)
    if latitude < -90 or latitude > 90:
        print(f"Error: Latitude ({latitude}) out of bounds. Must be between -90 and 90.")
        sys.exit(1)
    if precision < 1 or precision > 12:
        print("Error: Precision must be a number between 1 and 12.")
        sys.exit(1)
    
    result = get_geohash(latitude, longitude, precision)
    print(result)
        
    
if __name__ == '__main__':
    main()