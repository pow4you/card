from typing import *
from numbers import Number
 
import math
 
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
 
 
import scipy.stats as stat
import numpy as np
 
import re
 
 
class ImGen():
    def __init__(self, width, height, x, y, cov, intensity) -> None:
        self.width = width
        self.height = height
        self.i_mean = (x, y)
        self.cov = cov
        self.intensity = intensity
 
        self.center = None
        self.mean = None
        self.std = None
        self.var = None
        self.fwhm = None
        self.fried = None
 
        pass
 
    def get_image(self) -> List[List[Number]]:
        if True:
            x,y = np.mgrid[0:self.width:1, 0:self.height:1]
            pos = np.dstack((x,y))
 
            rv = stat.multivariate_normal(self.i_mean, self.cov)
 
            data = np.dstack(rv.pdf(pos) * (self.intensity/100) * 255)
 
            return np.array(*data)
        #except:
        #    return None
 
    def plot(self):
        x,y = np.mgrid[0:self.width:1, 0:self.height:1]
        pos = np.dstack((x,y))
 
        rv = stat.multivariate_normal(self.i_mean, self.cov)
 
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.contourf(x,y, rv.pdf(pos) * (self.intensity/100) * 255)
       
        plt.show()
        pass
 
    def save_results(self,
                    center:Tuple[Number,Number],
                    mean:Tuple[Number,Number],
                    std:Tuple[Number,Number],
                    var:Tuple[Number,Number],
                    fwhm:Tuple[Number,Number],
                    fried:Tuple[Number,Number] ):
        self.center = center
        self.mean = mean
        self.std = std
        self.var = var
        self.fwhm = fwhm
        self.fried = fried
       
 
class ImProc():
    def __init__(self) -> None:
        self.images: List[ImGen] = []
 
        self.wave_length = 5.32e-7 #m
        self.focal_length =  1.624 #m
        self.pixel_constant = 4.8e-6 #m
 
        self.fov_per_pixel = 2*math.atan(self.pixel_constant/(2*self.focal_length))
 
 
        pass
 
    def generate(self, num_samples:int, interpolate_values:List[str]):
 
        width = np.repeat(100,num_samples)
        height = np.repeat(100,num_samples)
 
        x = np.repeat(50,num_samples)
        y = np.repeat(50,num_samples)
 
        cov_a = np.repeat(100,num_samples)
        cov_b = np.repeat(1,num_samples)
        cov_c = np.repeat(1,num_samples)
        cov_d = np.repeat(100,num_samples)
 
        intensity = np.repeat(100,num_samples)
 
        range_axes = (1, 99)
        range_bigcov = (100, 1000)
        range_smlcov = (0.01, 99)
        range_intensity = (1, 200)
 
        random_pattern = r"random(?:_(\d+))?";
        for value in interpolate_values:
            match = re.match(random_pattern, value)
            if match:
                # If a seed is specified, extract it and use it to seed the random number generator
                seed = 0
                if match.group(1):
                    seed = int(match.group(1))
 
                np.random.seed(seed)
                all_possible_interpolations = ("x", "y", "cov_a", "cov_b", "cov_c", "cov_d", "intensity","-x", "-y", "-cov_a", "-cov_b", "-cov_c", "-cov_d", "-intensity","random_x", "random_y", "random_cov_a", "random_cov_b", "random_cov_c", "random_cov_d", "random_intensity" )
 
                interpolate_values.remove(value)
 
                num_to_choose = np.random.randint(1, len(all_possible_interpolations) + 1)
                selected_for_random_interpolation = set(np.random.choice(list(all_possible_interpolations), size=num_to_choose, replace=False))
                interpolate_values.extend(selected_for_random_interpolation)
 
 
 
        if "x" in interpolate_values:
            x = np.linspace(*range_axes, num_samples)
        elif "-x" in interpolate_values:
            x = np.linspace(*range_axes[::-1], num_samples)
        elif "random_x" in interpolate_values:
            x = np.random.uniform(*range_axes, num_samples)
 
        if "y" in interpolate_values:
            y = np.linspace(*range_axes, num_samples)
        elif "-y" in interpolate_values:
            y = np.linspace(*range_axes[::-1], num_samples)
        elif "random_y" in interpolate_values:
            y = np.random.uniform(*range_axes, num_samples)
 
        if "cov_a" in interpolate_values:
            cov_a = np.linspace(*range_bigcov, num_samples)
        elif "-cov_a" in interpolate_values:
            cov_a = np.linspace(*range_bigcov[::-1], num_samples)
        elif "random_cov_a" in interpolate_values:
            cov_a = np.random.uniform(*range_bigcov, num_samples)
 
        if "cov_b" in interpolate_values:
            cov_b = np.linspace(*range_smlcov, num_samples)
        elif "-cov_b" in interpolate_values:
            cov_b = np.linspace(*range_smlcov[::-1], num_samples)
        elif "random_cov_b" in interpolate_values:
            cov_b = np.random.uniform(*range_smlcov, num_samples)
 
        if "cov_c" in interpolate_values:
            cov_c = np.linspace(*range_smlcov, num_samples)
        elif "-cov_c" in interpolate_values:
            cov_c = np.linspace(*range_smlcov[::-1], num_samples)
        elif "random_cov_c" in interpolate_values:
            cov_c = np.random.uniform(*range_smlcov, num_samples)
 
        if "cov_d" in interpolate_values:
            cov_d = np.linspace(*range_bigcov, num_samples)
        elif "-cov_d" in interpolate_values:
            cov_d = np.linspace(*range_bigcov[::-1], num_samples)
        elif "random_cov_d" in interpolate_values:
            cov_d = np.random.uniform(*range_bigcov, num_samples)
 
        if "intensity" in interpolate_values:
            intensity = np.linspace(*range_intensity, num_samples)
        elif "-intensity" in interpolate_values:
            intensity = np.linspace(*range_intensity[::-1], num_samples)
        elif "random_intensity" in interpolate_values:
            intensity = np.random.uniform(*range_intensity, num_samples)
 
 
        for i in range(num_samples):
            self.images.append(
                ImGen(
                    width=width[i],
                    height=height[i],
 
                    x=x[i],
                    y=y[i],
 
                    cov=[
                        [cov_a[i],cov_b[i]],
                        [cov_c[i],cov_d[i]]
                    ],
 
                    intensity=intensity[i]
                )
            )
           
        pass
 
    def process_all(self, plot=False):
 
        result_set = []
        for i in range(len(self.images)):
            result_set.append(self.process_one(i))
       
        if plot:
            index = np.linspace(0, len(self.images), len(self.images))
            x_results, y_results = np.array(list(zip(*result_set)))
 
            center_x, max_x, mean_x, var_x, std_x, fwhm_x, fried_x = np.array(list(zip(*x_results)))
            center_y, max_y, mean_y, var_y, std_y, fwhm_y, fried_y = np.array(list(zip(*y_results)))
 
            fig = plt.figure(layout="constrained", figsize=(12, 18))
 
            gs = GridSpec(3, 3, figure=fig)
           
            axs00 = fig.add_subplot(gs[0, :1 ])
            axs00.plot(index, center_x, label='center x')
            axs00.plot(index, center_y, label='center y')
            axs02 = fig.add_subplot(gs[0, 2 ])
            axs02.plot(index, max_x, label='max intensity')
 
 
            axs10 = fig.add_subplot(gs[1, 0 ])
            axs10.plot(index, mean_x, label='mean x')
            axs10.plot(index, var_x, label='var x')
            axs10.plot(index, std_x, label='std x')
 
            axs11 = fig.add_subplot(gs[1, 1 ])
            axs11.plot(index, fwhm_x, label='fwhm x')
 
            axs12 = fig.add_subplot(gs[1, 2 ])
            axs12.plot(index, fried_x, label='fried x')
           
 
            axs20 = fig.add_subplot(gs[2, 0 ])
            axs20.plot(index, std_y, label='std y')
           
            axs21 = fig.add_subplot(gs[2, 1 ])
            axs21.plot(index, fwhm_y, label='fwhm y')
 
            axs22 = fig.add_subplot(gs[2, 2 ])
            axs22.plot(index, fried_y, label='fried y')
 
 
            for i, axs in enumerate(fig.axes):
                axs.legend()
                axs.tick_params()
 
 
            plt.show()
        pass
 
    def process_one(self, i):
        image:ImGen = self.images[i]
        data = image.get_image()
 
       
 
        width = image.width
        height = image.height
 
        center:Tuple[Number,Number] = (0,0)
 
        total_intensity = 0
        index_weighted_x_intensity = 0
        index_weighted_y_intensity = 0
 
        cols:List[Number] = [0]*height
        rows:List[Number] = [0]*width
 
        max_intensity = 0
 
        for y in range(height):
            for x in range(width):
                intensity = data[y][x]
 
                total_intensity += intensity
                index_weighted_x_intensity += (x+1) * intensity
                index_weighted_y_intensity += (y+1) * intensity
 
                if intensity > max_intensity :
                    max_intensity = intensity
 
                cols[y] += intensity
                rows[x] += intensity
       
        center = (
            index_weighted_x_intensity // total_intensity,
            index_weighted_y_intensity // total_intensity
        )# this is the mean u bingus
 
        col_intensity = 0
        index_weighted_col_intensity = 0
        for i in range(height):
            cols[i] /= width
            col_intensity += cols[i] # equi to full intensity
            index_weighted_col_intensity += cols[i]*(i+1) # equi to x intensity
 
 
        mean_x = index_weighted_col_intensity/col_intensity
 
        col_delta = 0
        for i in range(height):
            col_delta += cols[i] * math.pow(i - mean_x, 2)
 
        var_x = col_delta/col_intensity
        std_x = math.sqrt(var_x)*self.fov_per_pixel
        fwhm_x = 2*math.sqrt(2*math.log(2))*std_x
        fried_x = 0.98*(self.wave_length)/fwhm_x
 
 
        row_intensity = 0
        index_weighted_row_intensity = 0
        for i in range(width):
            rows[i] /= height
            row_intensity += rows[i]
            index_weighted_row_intensity += rows[i]*(i+1)
 
        mean_y = index_weighted_row_intensity/row_intensity
 
        row_delta = 0
        for i in range(width):
            row_delta += rows[i] * math.pow(i - mean_y, 2)
 
        var_y = row_delta/row_intensity
        std_y = math.sqrt(var_y) * self.fov_per_pixel
        fwhm_y = 2*math.sqrt(2*math.log(2))*std_y
        fried_y = 0.98*(self.wave_length)/fwhm_y
 
        self.images[i].save_results(
            center,
            (mean_x, mean_y),
            (var_x, var_y),
            (std_x, std_y),
            (fwhm_x, fwhm_y),
            (fried_x, fried_y)
        )
 
        return (
            (
                center[0],
                max_intensity,
                mean_x,
                var_x,
                std_x,
                fwhm_x,
                fried_x
            ),
            (
                center[1],
                max_intensity,
                mean_y,
                var_y,
                std_y,
                fwhm_y,
                fried_y
            )
        )
 
class SplitFunc(ImProc):
    def __init__(self) -> None:
        self.images: List[ImGen] = []
 
        self.wave_length = 5.32e-7 #m
        self.focal_length =  1.624 #m
        self.pixel_constant = 4.8e-6 #m
 
        self.fov_per_pixel = 2*math.atan(self.pixel_constant/(2*self.focal_length))
 
 
        pass
 
    def generate(self, num_samples:int, interpolate_values:List[str]):
 
        width = np.repeat(100,num_samples)
        height = np.repeat(100,num_samples)
 
        x = np.repeat(50,num_samples)
        y = np.repeat(50,num_samples)
 
        cov_a = np.repeat(100,num_samples)
        cov_b = np.repeat(1,num_samples)
        cov_c = np.repeat(1,num_samples)
        cov_d = np.repeat(100,num_samples)
 
        intensity = np.repeat(100,num_samples)
 
        range_axes = (1, 99)
        range_bigcov = (100, 1000)
        range_smlcov = (0.01, 99)
        range_intensity = (1, 200)
 
        random_pattern = r"random(?:_(\d+))?";
        for value in interpolate_values:
            match = re.match(random_pattern, value)
            if match:
                # If a seed is specified, extract it and use it to seed the random number generator
                seed = 0
                if match.group(1):
                    seed = int(match.group(1))
 
                np.random.seed(seed)
                all_possible_interpolations = ("x", "y", "cov_a", "cov_b", "cov_c", "cov_d", "intensity","-x", "-y", "-cov_a", "-cov_b", "-cov_c", "-cov_d", "-intensity","random_x", "random_y", "random_cov_a", "random_cov_b", "random_cov_c", "random_cov_d", "random_intensity" )
 
                interpolate_values.remove(value)
 
                num_to_choose = np.random.randint(1, len(all_possible_interpolations) + 1)
                selected_for_random_interpolation = set(np.random.choice(list(all_possible_interpolations), size=num_to_choose, replace=False))
                interpolate_values.extend(selected_for_random_interpolation)
 
 
 
        if "x" in interpolate_values:
            x = np.linspace(*range_axes, num_samples)
        elif "-x" in interpolate_values:
            x = np.linspace(*range_axes[::-1], num_samples)
        elif "random_x" in interpolate_values:
            x = np.random.uniform(*range_axes, num_samples)
 
        if "y" in interpolate_values:
            y = np.linspace(*range_axes, num_samples)
        elif "-y" in interpolate_values:
            y = np.linspace(*range_axes[::-1], num_samples)
        elif "random_y" in interpolate_values:
            y = np.random.uniform(*range_axes, num_samples)
 
        if "cov_a" in interpolate_values:
            cov_a = np.linspace(*range_bigcov, num_samples)
        elif "-cov_a" in interpolate_values:
            cov_a = np.linspace(*range_bigcov[::-1], num_samples)
        elif "random_cov_a" in interpolate_values:
            cov_a = np.random.uniform(*range_bigcov, num_samples)
 
        if "cov_b" in interpolate_values:
            cov_b = np.linspace(*range_smlcov, num_samples)
        elif "-cov_b" in interpolate_values:
            cov_b = np.linspace(*range_smlcov[::-1], num_samples)
        elif "random_cov_b" in interpolate_values:
            cov_b = np.random.uniform(*range_smlcov, num_samples)
 
        if "cov_c" in interpolate_values:
            cov_c = np.linspace(*range_smlcov, num_samples)
        elif "-cov_c" in interpolate_values:
            cov_c = np.linspace(*range_smlcov[::-1], num_samples)
        elif "random_cov_c" in interpolate_values:
            cov_c = np.random.uniform(*range_smlcov, num_samples)
 
        if "cov_d" in interpolate_values:
            cov_d = np.linspace(*range_bigcov, num_samples)
        elif "-cov_d" in interpolate_values:
            cov_d = np.linspace(*range_bigcov[::-1], num_samples)
        elif "random_cov_d" in interpolate_values:
            cov_d = np.random.uniform(*range_bigcov, num_samples)
 
        if "intensity" in interpolate_values:
            intensity = np.linspace(*range_intensity, num_samples)
        elif "-intensity" in interpolate_values:
            intensity = np.linspace(*range_intensity[::-1], num_samples)
        elif "random_intensity" in interpolate_values:
            intensity = np.random.uniform(*range_intensity, num_samples)
 
 
        for i in range(num_samples):
            self.images.append(
                ImGen(
                    width=width[i],
                    height=height[i],
 
                    x=x[i],
                    y=y[i],
 
                    cov=[
                        [cov_a[i],cov_b[i]],
                        [cov_c[i],cov_d[i]]
                    ],
 
                    intensity=intensity[i]
                )
            )
           
        pass
 
    def process_all(self, plot=False):
 
        result_set = []
        for i in range(len(self.images)):
            result_set.append(self.process_one(i))
       
        if plot:
            index = np.linspace(0, len(self.images), len(self.images))
            x_results, y_results = np.array(list(zip(*result_set)))
 
            center_x, max_x, mean_x, var_x, std_x, fwhm_x, fried_x = np.array(list(zip(*x_results)))
            center_y, max_y, mean_y, var_y, std_y, fwhm_y, fried_y = np.array(list(zip(*y_results)))
 
            fig = plt.figure(layout="constrained", figsize=(12, 18))
 
            gs = GridSpec(3, 3, figure=fig)
           
            axs00 = fig.add_subplot(gs[0, :1 ])
            axs00.plot(index, center_x, label='center x')
            axs00.plot(index, center_y, label='center y')
            axs02 = fig.add_subplot(gs[0, 2 ])
            axs02.plot(index, max_x, label='max intensity')
 
 
            axs10 = fig.add_subplot(gs[1, 0 ])
            axs10.plot(index, mean_x, label='mean x')
            axs10.plot(index, var_x, label='var x')
            axs10.plot(index, std_x, label='std x')
 
            axs11 = fig.add_subplot(gs[1, 1 ])
            axs11.plot(index, fwhm_x, label='fwhm x')
 
            axs12 = fig.add_subplot(gs[1, 2 ])
            axs12.plot(index, fried_x, label='fried x')
           
 
            axs20 = fig.add_subplot(gs[2, 0 ])
            axs20.plot(index, std_y, label='std y')
           
            axs21 = fig.add_subplot(gs[2, 1 ])
            axs21.plot(index, fwhm_y, label='fwhm y')
 
            axs22 = fig.add_subplot(gs[2, 2 ])
            axs22.plot(index, fried_y, label='fried y')
 
 
            for i, axs in enumerate(fig.axes):
                axs.legend()
                axs.tick_params()
 
 
            plt.show()
        pass
 
    def process_one(self, i):
        image:ImGen = self.images[i]
        data = image.get_image()
 
       
 
        width = image.width
        height = image.height
 
        center:Tuple[Number,Number] = (0,0)
 
        total_intensity = 0
        index_weighted_x_intensity = 0
        index_weighted_y_intensity = 0
 
        max_intensity = 0
 
        for y in range(height):
            for x in range(width):
                intensity = data[y][x]
 
                total_intensity += intensity
                index_weighted_x_intensity += (x+1) * intensity
                index_weighted_y_intensity += (y+1) * intensity
 
                if intensity > max_intensity :
                    max_intensity = intensity
       
        mean_x = index_weighted_x_intensity / total_intensity
        mean_y = index_weighted_y_intensity / total_intensity


        
        x_delta = 0
        y_delta = 0
        for y in range(height):
            for x in range(width):
                intensity = data[y][x]
 
                x_delta += intensity * math.pow(x - mean_x, 2)
                y_delta += intensity * math.pow(y - mean_y, 2)
        
        
        var_x = x_delta / total_intensity
        std_x = math.sqrt(var_x)*self.fov_per_pixel
        fwhm_x = 2*math.sqrt(2*math.log(2))*std_x
        fried_x = 0.98*(self.wave_length)/fwhm_x
 
        var_y = y_delta / total_intensity
        std_y = math.sqrt(var_y) * self.fov_per_pixel
        fwhm_y = 2*math.sqrt(2*math.log(2))*std_y
        fried_y = 0.98*(self.wave_length)/fwhm_y
 
        self.images[i].save_results(
            center,
            (mean_x, mean_y),
            (var_x, var_y),
            (std_x, std_y),
            (fwhm_x, fwhm_y),
            (fried_x, fried_y)
        )
 
        return (
            (
                center[0],
                max_intensity,
                mean_x,
                var_x,
                std_x,
                fwhm_x,
                fried_x
            ),
            (
                center[1],
                max_intensity,
                mean_y,
                var_y,
                std_y,
                fwhm_y,
                fried_y
            )
        )
 
 
if __name__ == "__main__":
    total_images = 100
    selected_images = 20
 
    sim = SplitFunc()
    sim.generate(total_images,["-cov_a", "cov_d"])
   
 
    images = [image.get_image() for image in sim.images]
 
    indices = np.linspace(0, total_images - 1, selected_images, dtype=int)
    selected = [images[i] for i in indices]
 
    fig, axs = plt.subplots(4, 5, figsize=(15, 12))
    for i, image in enumerate(selected):
 
        row = i // 5
        col = i % 5
 
        axs[row, col].imshow(image, cmap='viridis')
        axs[row, col].set_title(f'Image {indices[i]+1}')
        axs[row, col].axis('off')
   
    plt.tight_layout()
    plt.show()
 
 
    sim.process_all(True)
 
    sim = ImProc()
    sim.generate(total_images,["-cov_a", "cov_d"])
    sim.process_all(True)
 
       

