from netCDF4 import Dataset
import numpy as np


if __name__ == '__main__':
    base_names = 'test', 'train'
    for base_name in base_names:
        np_file_name = base_name + '_data_trend.npz'
        data_np = np.load(np_file_name)['data']
        print(data_np.shape)
        ncfile = Dataset('deposition/{}.nc'.format(base_name), mode='w', format='NETCDF4_CLASSIC')
        # = ncfile.createDimension('lat', 73)  # latitude axis
        md_dim = ncfile.createDimension('md', data_np.shape[1])  # md
        realization_dim = ncfile.createDimension('realization', data_np.shape[0])  # realization number


        # self.angle
        angle = ncfile.createVariable('angle', np.float64, ('realization', 'md'))  # note: unlimited dimension is leftmost
        angle.units = 'rad'
        angle[:, :] = data_np[:, :, 0]
        # self.position
        svd = ncfile.createVariable('svd', np.float64, ('realization', 'md'))  # note: unlimited dimension is leftmost
        svd.units = 'ft'
        svd[:, :] = data_np[:, :, 1]
        # self.thl
        vs = ncfile.createVariable('vs', np.float64, ('realization', 'md'))  # note: unlimited dimension is leftmost
        vs.units = 'ft'
        svd[:, :] = data_np[:, :, 2]
        print(ncfile)


