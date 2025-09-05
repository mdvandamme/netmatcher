# -*- coding: utf-8 -*-

import shapely




def hausdorff(line1, line2):
    return shapely.hausdorff_distance(line1, line2)

