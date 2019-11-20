import pandas as pd

# Downloaded colors and CSS from: 
# https://htmlcolorcodes.com/color-chart/

def get_colors():
    css = '''
        /* Red */
        .red { color: #f44336; }
        .red-50 { color: #ffebee; }
        .red-100 { color: #ffcdd2; }
        .red-200 { color: #ef9a9a; }
        .red-300 { color: #e57373; }
        .red-400 { color: #ef5350; }
        .red-500 { color: #f44336; }
        .red-600 { color: #e53935; }
        .red-700 { color: #d32f2f; }
        .red-800 { color: #c62828; }
        .red-900 { color: #b71c1c; }
        .red-a100 { color: #ff8a80; }
        .red-a200 { color: #ff5252; }
        .red-a400 { color: #ff1744; }
        .red-a700 { color: #d50000; }

        /* Pink */
        .pink { color: #e91e63; }
        .pink-50 { color: #fce4ec; }
        .pink-100 { color: #f8bbd0; }
        .pink-200 { color: #f48fb1; }
        .pink-300 { color: #f06292; }
        .pink-400 { color: #ec407a; }
        .pink-500 { color: #e91e63; }
        .pink-600 { color: #d81b60; }
        .pink-700 { color: #c2185b; }
        .pink-800 { color: #ad1457; }
        .pink-900 { color: #880e4f; }
        .pink-a100 { color: #ff80ab; }
        .pink-a200 { color: #ff4081; }
        .pink-a400 { color: #f50057; }
        .pink-a700 { color: #c51162; }

        /* Purple */
        .purple { color: #9c27b0; }
        .purple-50 { color: #f3e5f5; }
        .purple-100 { color: #e1bee7; }
        .purple-200 { color: #ce93d8; }
        .purple-300 { color: #ba68c8; }
        .purple-400 { color: #ab47bc; }
        .purple-500 { color: #9c27b0; }
        .purple-600 { color: #8e24aa; }
        .purple-700 { color: #7b1fa2; }
        .purple-800 { color: #6a1b9a; }
        .purple-900 { color: #4a148c; }
        .purple-a100 { color: #ea80fc; }
        .purple-a200 { color: #e040fb; }
        .purple-a400 { color: #d500f9; }
        .purple-a700 { color: #aa00ff; }

        /* Deep Purple */
        .deep-purple { color: #673ab7; }
        .deep-purple-50 { color: #ede7f6; }
        .deep-purple-100 { color: #d1c4e9; }
        .deep-purple-200 { color: #b39ddb; }
        .deep-purple-300 { color: #9575cd; }
        .deep-purple-400 { color: #7e57c2; }
        .deep-purple-500 { color: #673ab7; }
        .deep-purple-600 { color: #5e35b1; }
        .deep-purple-700 { color: #512da8; }
        .deep-purple-800 { color: #4527a0; }
        .deep-purple-900 { color: #311b92; }
        .deep-purple-a100 { color: #b388ff; }
        .deep-purple-a200 { color: #7c4dff; }
        .deep-purple-a400 { color: #651fff; }
        .deep-purple-a700 { color: #6200ea; }

        /* Indigo */
        .indigo { color: #3f51b5; }
        .indigo-50 { color: #e8eaf6; }
        .indigo-100 { color: #c5cae9; }
        .indigo-200 { color: #9fa8da; }
        .indigo-300 { color: #7986cb; }
        .indigo-400 { color: #5c6bc0; }
        .indigo-500 { color: #3f51b5; }
        .indigo-600 { color: #3949ab; }
        .indigo-700 { color: #303f9f; }
        .indigo-800 { color: #283593; }
        .indigo-900 { color: #1a237e; }
        .indigo-a100 { color: #8c9eff; }
        .indigo-a200 { color: #536dfe; }
        .indigo-a400 { color: #3d5afe; }
        .indigo-a700 { color: #304ffe; }

        /* Blue */
        .blue { color: #2196f3; }
        .blue-50 { color: #e3f2fd; }
        .blue-100 { color: #bbdefb; }
        .blue-200 { color: #90caf9; }
        .blue-300 { color: #64b5f6; }
        .blue-400 { color: #42a5f5; }
        .blue-500 { color: #2196f3; }
        .blue-600 { color: #1e88e5; }
        .blue-700 { color: #1976d2; }
        .blue-800 { color: #1565c0; }
        .blue-900 { color: #0d47a1; }
        .blue-a100 { color: #82b1ff; }
        .blue-a200 { color: #448aff; }
        .blue-a400 { color: #2979ff; }
        .blue-a700 { color: #2962ff; }

        /* Light Blue */
        .light-blue { color: #03a9f4; }
        .light-blue-50 { color: #e1f5fe; }
        .light-blue-100 { color: #b3e5fc; }
        .light-blue-200 { color: #81d4fa; }
        .light-blue-300 { color: #4fc3f7; }
        .light-blue-400 { color: #29b6f6; }
        .light-blue-500 { color: #03a9f4; }
        .light-blue-600 { color: #039be5; }
        .light-blue-700 { color: #0288d1; }
        .light-blue-800 { color: #0277bd; }
        .light-blue-900 { color: #01579b; }
        .light-blue-a100 { color: #80d8ff; }
        .light-blue-a200 { color: #40c4ff; }
        .light-blue-a400 { color: #00b0ff; }
        .light-blue-a700 { color: #0091ea; }

        /* Cyan */
        .cyan { color: #00bcd4; }
        .cyan-50 { color: #e0f7fa; }
        .cyan-100 { color: #b2ebf2; }
        .cyan-200 { color: #80deea; }
        .cyan-300 { color: #4dd0e1; }
        .cyan-400 { color: #26c6da; }
        .cyan-500 { color: #00bcd4; }
        .cyan-600 { color: #00acc1; }
        .cyan-700 { color: #0097a7; }
        .cyan-800 { color: #00838f; }
        .cyan-900 { color: #006064; }
        .cyan-a100 { color: #84ffff; }
        .cyan-a200 { color: #18ffff; }
        .cyan-a400 { color: #00e5ff; }
        .cyan-a700 { color: #00b8d4; }

        /* Teal */
        .teal { color: #009688; }
        .teal-50 { color: #e0f2f1; }
        .teal-100 { color: #b2dfdb; }
        .teal-200 { color: #80cbc4; }
        .teal-300 { color: #4db6ac; }
        .teal-400 { color: #26a69a; }
        .teal-500 { color: #009688; }
        .teal-600 { color: #00897b; }
        .teal-700 { color: #00796b; }
        .teal-800 { color: #00695c; }
        .teal-900 { color: #004d40; }
        .teal-a100 { color: #a7ffeb; }
        .teal-a200 { color: #64ffda; }
        .teal-a400 { color: #1de9b6; }
        .teal-a700 { color: #00bfa5; }

        /* Green */
        .green { color: #4caf50; }
        .green-50 { color: #e8f5e9; }
        .green-100 { color: #c8e6c9; }
        .green-200 { color: #a5d6a7; }
        .green-300 { color: #81c784; }
        .green-400 { color: #66bb6a; }
        .green-500 { color: #4caf50; }
        .green-600 { color: #43a047; }
        .green-700 { color: #388e3c; }
        .green-800 { color: #2e7d32; }
        .green-900 { color: #1b5e20; }
        .green-a100 { color: #b9f6ca; }
        .green-a200 { color: #69f0ae; }
        .green-a400 { color: #00e676; }
        .green-a700 { color: #00c853; }

        /* Light Green */
        .light-green { color: #8bc34a; }
        .light-green-50 { color: #f1f8e9; }
        .light-green-100 { color: #dcedc8; }
        .light-green-200 { color: #c5e1a5; }
        .light-green-300 { color: #aed581; }
        .light-green-400 { color: #9ccc65; }
        .light-green-500 { color: #8bc34a; }
        .light-green-600 { color: #7cb342; }
        .light-green-700 { color: #689f38; }
        .light-green-800 { color: #558b2f; }
        .light-green-900 { color: #33691e; }
        .light-green-a100 { color: #ccff90; }
        .light-green-a200 { color: #b2ff59; }
        .light-green-a400 { color: #76ff03; }
        .light-green-a700 { color: #64dd17; }

        /* Lime */
        .lime { color: #cddc39; }
        .lime-50 { color: #f9fbe7; }
        .lime-100 { color: #f0f4c3; }
        .lime-200 { color: #e6ee9c; }
        .lime-300 { color: #dce775; }
        .lime-400 { color: #d4e157; }
        .lime-500 { color: #cddc39; }
        .lime-600 { color: #c0ca33; }
        .lime-700 { color: #afb42b; }
        .lime-800 { color: #9e9d24; }
        .lime-900 { color: #827717; }
        .lime-a100 { color: #f4ff81; }
        .lime-a200 { color: #eeff41; }
        .lime-a400 { color: #c6ff00; }
        .lime-a700 { color: #aeea00; }

        /* Yellow */
        .yellow { color: #ffeb3b; }
        .yellow-50 { color: #fffde7; }
        .yellow-100 { color: #fff9c4; }
        .yellow-200 { color: #fff59d; }
        .yellow-300 { color: #fff176; }
        .yellow-400 { color: #ffee58; }
        .yellow-500 { color: #ffeb3b; }
        .yellow-600 { color: #fdd835; }
        .yellow-700 { color: #fbc02d; }
        .yellow-800 { color: #f9a825; }
        .yellow-900 { color: #f57f17; }
        .yellow-a100 { color: #ffff8d; }
        .yellow-a200 { color: #ffff00; }
        .yellow-a400 { color: #ffea00; }
        .yellow-a700 { color: #ffd600; }

        /* Amber */
        .amber { color: #ffc107; }
        .amber-50 { color: #fff8e1; }
        .amber-100 { color: #ffecb3; }
        .amber-200 { color: #ffe082; }
        .amber-300 { color: #ffd54f; }
        .amber-400 { color: #ffca28; }
        .amber-500 { color: #ffc107; }
        .amber-600 { color: #ffb300; }
        .amber-700 { color: #ffa000; }
        .amber-800 { color: #ff8f00; }
        .amber-900 { color: #ff6f00; }
        .amber-a100 { color: #ffe57f; }
        .amber-a200 { color: #ffd740; }
        .amber-a400 { color: #ffc400; }
        .amber-a700 { color: #ffab00; }

        /* Orange */
        .orange { color: #ff9800; }
        .orange-50 { color: #fff3e0; }
        .orange-100 { color: #ffe0b2; }
        .orange-200 { color: #ffcc80; }
        .orange-300 { color: #ffb74d; }
        .orange-400 { color: #ffa726; }
        .orange-500 { color: #ff9800; }
        .orange-600 { color: #fb8c00; }
        .orange-700 { color: #f57c00; }
        .orange-800 { color: #ef6c00; }
        .orange-900 { color: #e65100; }
        .orange-a100 { color: #ffd180; }
        .orange-a200 { color: #ffab40; }
        .orange-a400 { color: #ff9100; }
        .orange-a700 { color: #ff6d00; }

        /* Deep Orange */
        .deep-orange { color: #ff5722; }
        .deep-orange-50 { color: #fbe9e7; }
        .deep-orange-100 { color: #ffccbc; }
        .deep-orange-200 { color: #ffab91; }
        .deep-orange-300 { color: #ff8a65; }
        .deep-orange-400 { color: #ff7043; }
        .deep-orange-500 { color: #ff5722; }
        .deep-orange-600 { color: #f4511e; }
        .deep-orange-700 { color: #e64a19; }
        .deep-orange-800 { color: #d84315; }
        .deep-orange-900 { color: #bf360c; }
        .deep-orange-a100 { color: #ff9e80; }
        .deep-orange-a200 { color: #ff6e40; }
        .deep-orange-a400 { color: #ff3d00; }
        .deep-orange-a700 { color: #dd2c00; }

        /* Brown */
        .brown { color: #795548; }
        .brown-50 { color: #efebe9; }
        .brown-100 { color: #d7ccc8; }
        .brown-200 { color: #bcaaa4; }
        .brown-300 { color: #a1887f; }
        .brown-400 { color: #8d6e63; }
        .brown-500 { color: #795548; }
        .brown-600 { color: #6d4c41; }
        .brown-700 { color: #5d4037; }
        .brown-800 { color: #4e342e; }
        .brown-900 { color: #3e2723; }

        /* Grey */
        .grey { color: #9e9e9e; }
        .grey-50 { color: #fafafa; }
        .grey-100 { color: #f5f5f5; }
        .grey-200 { color: #eeeeee; }
        .grey-300 { color: #e0e0e0; }
        .grey-400 { color: #bdbdbd; }
        .grey-500 { color: #9e9e9e; }
        .grey-600 { color: #757575; }
        .grey-700 { color: #616161; }
        .grey-800 { color: #424242; }
        .grey-900 { color: #212121; }

        /* Blue Grey */
        .blue-grey { color: #607d8b; }
        .blue-grey-50 { color: #eceff1; }
        .blue-grey-100 { color: #cfd8dc; }
        .blue-grey-200 { color: #b0bec5; }
        .blue-grey-300 { color: #90a4ae; }
        .blue-grey-400 { color: #78909c; }
        .blue-grey-500 { color: #607d8b; }
        .blue-grey-600 { color: #546e7a; }
        .blue-grey-700 { color: #455a64; }
        .blue-grey-800 { color: #37474f; }
        .blue-grey-900 { color: #263238; }
    '''
    lines = css.split('\n')[1:-1]
    lines = [line.strip() for line in lines]
    colors = []
    for (i,line) in enumerate(lines):
        if line.startswith('/*'):
            color_family = line[3:-3]
        elif line.startswith('.'):
            chunks = line.split()
            color_name = chunks[0][1:]
            color_code = chunks[3][:-1]
            colors.append({
                'color_family':color_family,
                'color_name':color_name,
                'color_code':color_code
            })
    colors = pd.DataFrame(colors)
    return colors

def get_n_contrasting_colors(n):
    colors = get_colors()
    color_family_groups = colors.groupby('color_family').groups

    # Manually set the order for iterating through the families
    # Omitted color familes: Yellow, Grey, Brown, Blue Grey
    color_family_order = [
        'Red',
        'Light Blue',
        'Deep Orange',
        'Blue',
        'Amber',
        'Purple',
        'Teal',
        'Orange',
        'Green',
        'Pink',
        'Cyan',
        'Indigo',
        'Light Green',
        'Deep Purple',
        'Lime',
    ]

    # Manually set the order for iterating through the shades
    color_shades = [4,6,8,5,7,9] # assumes at least 10 shades (0 through 9)

    # Iterate through families and shades
    n_families = len(color_family_order)
    n_shades = len(color_shades)
    indexes = []
    for i in range(n):
        f = i%n_families # iterate in order
        s = (i//n_families)%n_shades # only increment shade after iterating over all families
        family = color_family_order[f]
        shade = color_shades[s]
        if len(indexes)>=n:
            break
        else:
            indexes.append(color_family_groups[family][shade])
            
    selected_colors = colors.loc[indexes]
    return selected_colors


