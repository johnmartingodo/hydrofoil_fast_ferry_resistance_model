# © 2023, NTNU
# Author: John Martin Kleven Godø <john.martin.godo@ntnu.no; john.martin.kleven.godo@gmail.com>
# This code is licenced under EUROPEAN UNION PUBLIC LICENCE v. 1.2

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import LinearNDInterpolator
line_width = 2.0
font_size = 20
label_font_size = 20
figure_size = (7, 5)

class DataExtractor():
    def __init__(self, root_dir, p1_fnm, p2_fnm, d_fnm):
        self.root_dir = root_dir
        self.p1_fnm = p1_fnm
        self.p2_fnm = p2_fnm
        self.d_fnm = d_fnm
    
        if self.root_dir[-1] != '/':
            self.root_dir += '/'
        self.read_data()

    
    # -------------------------------------------------------------------------
    # Reading and plotting
    # -------------------------------------------------------------------------
    def read_data(self):
        ''' Read arrays from files '''
        self.p1_array = np.load(self.root_dir + self.p1_fnm)
        self.p2_array = np.load(self.root_dir + self.p2_fnm)
        self.d_array = np.load(self.root_dir + self.d_fnm)

        if (np.shape(self.p1_array) != np.shape(self.p2_array) or 
            np.shape(self.p1_array) != np.shape(self.p2_array)):
            raise ValueError('The input arrays must have equal dimensions')
        
        self.n_dim1, self.n_dim2 = np.shape(self.p1_array)

    def plot_data(self):
        ''' Plot data as a function of p1 and p2'''
        self.make_contour_plot(self.p1_array, self.p1_fnm,
                               self.p2_array, self.p2_fnm,
                               self.d_array, self.d_fnm)

    def make_contour_plot(self, 
                          x_plot, x_label, 
                          y_plot, y_label, 
                          z_plot, z_label):
        ''' Create a contour plot of z_plot as a function of x_plot and y_plot'''
        fig, ax = plt.subplots(1, 1, figsize = figure_size)
        cp = ax.contour(x_plot, y_plot, z_plot)
        ax.clabel(cp, inline = True, fontsize = label_font_size)
        ax.set_xlabel(x_label, fontsize = label_font_size)
        ax.set_ylabel(y_label, fontsize = label_font_size)
        if z_label != None:
            ax.set_title(z_label, fontsize = label_font_size)
        ax.tick_params(axis='both', which='major', labelsize=label_font_size)
        ax.grid(alpha = 0.5)
        fig.tight_layout()
    
    
    
    # -------------------------------------------------------------------------
    # Data interpolation
    # -------------------------------------------------------------------------
    def create_interpolator(self):
        n_pcomb = self.n_dim1 * self.n_dim2
        pcomb_list = np.zeros((n_pcomb, 2))
        d_list = np.zeros(n_pcomb)
        counter = 0
        for i in range(self.n_dim1):
            for j in range(self.n_dim2):
                p1_val_cur = self.p1_array[i, j]
                p2_val_cur = self.p2_array[i, j]
                d_val_cur = self.d_array[i, j]
                pcomb_list[counter] = np.array((p1_val_cur, p2_val_cur))
                d_list[counter] = d_val_cur
                counter += 1
        
        self.interpolator = LinearNDInterpolator(pcomb_list, 
                                                 d_list, 
                                                 rescale=True)
    
    def get_interpolated_points(self, p1_val, p2_val):
        return self.interpolator(p1_val, p2_val)

    # -------------------------------------------------------------------------
    # Data extraction
    # -------------------------------------------------------------------------
    def get_arrays(self):
        return self.p1_array, self.p2_array, self.d_array