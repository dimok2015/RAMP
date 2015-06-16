# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:55:23 2015

@author: dmitry
"""
import numpy as np

en_lat_bottom = -5
en_lat_top = 5
en_lon_left = 360 - 170
en_lon_right = 360 - 120


def get_enso_mean(tas):
    """The array of mean temperatures in the El Nino 3.4 region at all time points."""
    return tas.loc[:, en_lat_bottom:en_lat_top, en_lon_left:en_lon_right].mean(dim=('lat','lon'))


class FeatureExtractor(object):

    def __init__(self):
        pass

    def fit(self, temperatures_xray, n_burn_in, n_lookahead):
        pass

    def transform(self, temperatures_xray, n_burn_in, n_lookahead, skf_is):
        """Use world temps as features."""
        # Set all temps on world map as features
        all_temps = temperatures_xray['tas'].values
        time_steps, lats, lons = all_temps.shape
        all_temps = all_temps.reshape((time_steps,lats*lons))
        all_temps = all_temps[n_burn_in:-n_lookahead,:]
        time_steps, temps = all_temps.shape

        data = []
        lag = 0
        if lag == 0:
            temp_list = np.zeros((time_steps,temps))
            for i in range(0,time_steps):
                temp_list[i,:] = all_temps[i,:]
        else:
            temp_list = np.zeros((time_steps-lag,(lag+1)*temps))
            for i in range(lag,time_steps):
                temp_list[i-lag,:] = all_temps[i-lag:i+1,:].reshape(((lag+1)*temps))

        data.append(temp_list)

        return data[0]
