import struct
import csv
import os

def read_dat_file_to_csv(input_file):
  print(f"Начато преобразование файла...")
  with open(input_file, "rb") as f:
      data = f.read()

  apid = os.path.basename(input_file).split(".")[0].split("_")[2]
  offset = 0
  row_count = 0

  output_file = os.path.join(os.path.dirname(input_file), f"{os.path.splitext(os.path.basename(input_file))[0]}.csv")
  with open(output_file, "w", newline='') as csvfile:
      csvwriter = csv.writer(csvfile, escapechar=',', quoting=csv.QUOTE_NONE)
      row1 = [
          #"P-field", "Days from 01/01/1950", "Millis in day",
          "UT time of the first point of the data array", "Orbit number", #"Sub-orbit type", "Telemetry station",
          #"Version of the processing software", "Sub-version of the processing software", "Version of the calibration file", "Sub-version of the calibration file",

          "Latitude", "Longitude", "Altitude", #"Local time of the first point of the data array",
          #"Geomagnetic latitude", "Geomagnetic longitude", "Magnetic local time of the first point of the data array",
          #"Invariant latitude", "Mc Ilwain parameter", "Geocentric latitude (conjugate)",
          #"Geocentric longitude (conjugate)", "Geocentric latitude (north conjugate)",
          #"Geocentric longitude (north conjugate)", "Geocentric latitude (south conjugate)",
          #"Geocentric longitude (south conjugate)",
          #"Magnetic field", "Proton gyrofrequency",
          #"Solar position", "Software Component Version", "Software Component sub-version",

          #"Msat2geo Matrix", "Mgeo2lgm Matrix", "Quality Index", "Software Version", "Software Subversion"
      ]
      row1_1129 = [
          "Data Type",
          #"House Keepings and Status",
          "Data coordinate system",
          "Matrix from sensor to satellite coordinate systems",
          "Data unit",
          "Sampling frequency",
          "Sample data number per component",
          "Time duration of one data array",
          "First component name",
          "Waveform sample array of the first component",
          "Second component name",
          "Waveform sample array of the second component",
          "Third component name",
          "Waveform sample array of the third component",
          "Probe 1 name",
          "Potential array of the E1 probe",
          "Probe 2 name",
          "Potential array of the E2 probe",
          "Probe 3 name",
          "Potential array of the E3 probe",
          "Probe 4 name",
          "Potential array of the E4 probe"
      ]
      row1_1130 = [
          "Data Type",
          #"House Keepings and Status",
          "Data coordinate system",
          "Matrix from sensor to satellite coordinate systems",
          "Data unit",
          "Sampling frequency",
          "Sample data number per component",
          "Time duration of one data array",
          "First component name",
          "Waveform sample array of the first component",
          "Second component name",
          "Waveform sample array of the second component",
          "Third component name",
          "Waveform sample array of the third component"
      ]
      row1_1131 = [
          "Data Type",
          #"House Keepings and Status",
          "Data coordinate system",
          "Data unit",
          "Sampling frequency",
          "Sample data number per component",
          "Time duration of one data array",
          "Component name",
          "Waveform sample array"
      ]
      row1_1132 = [
          "Data Type",
          #"House Keepings and Status",
          "Data coordinate system",
          "Component name",
          "Data unit",
          "Number of consecutive spectra (Nb)",
          "Number of spectrum frequencies (Nbf)",
          "Total time duration of Nb spectra",
          "Frequency resolution",
          "Frequency range",
          "UT time of the first spectrum"
      ]
      row1_1138 = [
          "Data Type",
          #"House Keepings and Status",
          "Data sub_type"
      ]
      row1_1139 = [
          "Data Type",
          #"House Keepings and Status",
          "Time resolution",
          "Density unit",
          "Temperature unit",
          "Velocity unit",
          "Potential unit",
          "Angle unit",
          "H+ density", "He+ density", "O+ density",
          "Ions temperature",
          "Ions velocity along the satellite Oz axis",
          "Angle between the ion velocity and -Oz axis of satellite", "Angle between projection of the ions velocity on the plane xOy and axis Ox of satellite",
          "Satellite potential"
      ]
      row1_1141 = [
          "Data Type",
          #"House Keepings and Status",
          "Time resolution",
          "Polarisation voltage",
          "Descrimination level",
          "Spectum data unit",
          "Pitch angle unit",
          "Spectrum 1", "Spectrum 2", "Spectrum 3", "Spectrum 4",
          "Energy table",
          "Pitch angle"
      ]
      row1_1142 = [
          "Data Type",
          #"House Keepings and Status",
          "Spectrum time resolution",
          "Counters time resolution",
          "Polarisation voltage",
          "Descrimination level",
          "Threshold low interval 1",
          "Threshold low interval 2",
          "Threshold low interval 3",
          "Threshold high interval 3",
          "Spectum data unit",
          "Pitch angle unit",
          "Counters 1", "Spectrum 1",
          "Counters 2", "Spectrum 2",
          "Counters 3", "Spectrum 3",
          "Counters 4", "Spectrum 4",
          "Counters 5", "Spectrum 5",
          "Counters 6", "Spectrum 6",
          "Counters 7", "Spectrum 7",
          "Energy table",
          "Pitch angle"
      ]
      row1_1143 = [
          "Data Type",
          #"House Keepings and Status",
          "Time resolution",
          "Density unit",
          "Temperature unit",
          "Potentional unit",
          "Electron density", "Ion density",
          "Electron temperature", "Plasma potential",
          "Floating potential", "Satellite potential"
      ]
      match (apid):
        case "1129":
          row1 += row1_1129
        case "1130":
          row1 += row1_1130
        case "1131":
          row1 += row1_1131
        case "1132":
          row1 += row1_1132
        case "1133":
          row1 += row1_1131
        case "1134":
          row1 += row1_1132
        case "1135":
          row1 += row1_1130
        case "1136":
          row1 += row1_1131
        case "1137":
          row1 += row1_1132
        case "1138":
          row1 += row1_1138
        case "1139":
          row1 += row1_1139
        case "1140":
          row1 += row1_1139
        case "1141":
          row1 += row1_1141
        case "1142":
          row1 += row1_1142
        case "1143":
          row1 += row1_1143
        case "1144":
          row1 += row1_1143
        case _:
          print("APID файла не распознан")
      csvwriter.writerow(row1)
      row2 = []
      while offset < len(data):
        # General Header
        #p_field = struct.unpack_from(">B", data, offset)[0]
        #row2.append(p_field)
        offset += 1
        #days_from_1950 = struct.unpack_from(">I", b'\x00' + data[offset:offset + 3])[0]
        #row2.append(days_from_1950)
        offset += 3
        #millis_in_day = struct.unpack_from("<I", data, offset)[0]
        #row2.append(millis_in_day)
        offset += 4
        year = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        month = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        day = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        hour = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        minute = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        second = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        millisecond = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        row2.append(f"{year}-{month}-{day}-{hour}-{minute}-{second}-{millisecond}")
        orbit_number = struct.unpack_from(">H", data, offset)[0]
        row2.append(orbit_number)
        offset += 2
        #sub_orbit_type = struct.unpack_from(">B", data, offset)[0]
        #row2.append(sub_orbit_type)
        offset += 2
        #telemetry_station = struct.unpack_from("8s", data, offset)[0].decode('windows-1251').strip()
        #row2.append(telemetry_station)
        offset += 8
        #software_version = struct.unpack_from(">B", data, offset)[0]
        #row2.append(software_version)
        offset += 1
        #software_sub_version = struct.unpack_from(">B", data, offset)[0]
        #row2.append(software_sub_version)
        offset += 1
        #calibration_version = struct.unpack_from(">B", data, offset)[0]
        #row2.append(calibration_version)
        offset += 1
        #calibration_sub_version = struct.unpack_from(">B", data, offset)[0]
        #row2.append(calibration_sub_version)
        offset += 1

        # Orbital Parameters
        latitude = struct.unpack_from(">f", data, offset)[0]
        row2.append(latitude)
        offset += 4
        longitude = struct.unpack_from(">f", data, offset)[0]
        row2.append(longitude)
        offset += 4
        altitude = struct.unpack_from(">f", data, offset)[0]
        row2.append(altitude)
        offset += 4
        #local_time = struct.unpack_from(">f", data, offset)[0]
        #row2.append(local_time)
        offset += 4
        #geomagnetic_latitude = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geomagnetic_latitude)
        offset += 4
        #geomagnetic_longitude = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geomagnetic_longitude)
        offset += 4
        #magnetic_local_time = struct.unpack_from(">f", data, offset)[0]
        #row2.append(magnetic_local_time)
        offset += 4
        #invariant_latitude = struct.unpack_from(">f", data, offset)[0]
        #row2.append(invariant_latitude)
        offset += 4
        #mc_ilwain_parameter = struct.unpack_from(">f", data, offset)[0]
        #row2.append(mc_ilwain_parameter)
        offset += 4
        #geocentric_latitude_conjugate = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geocentric_latitude_conjugate)
        offset += 4
        #geocentric_longitude_conjugate = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geocentric_longitude_conjugate)
        offset += 4
        #geocentric_latitude_north_conjugate = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geocentric_latitude_north_conjugate)
        offset += 4
        #geocentric_longitude_north_conjugate = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geocentric_longitude_north_conjugate)
        offset += 4
        #geocentric_latitude_south_conjugate = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geocentric_latitude_south_conjugate)
        offset += 4
        #geocentric_longitude_south_conjugate = struct.unpack_from(">f", data, offset)[0]
        #row2.append(geocentric_longitude_south_conjugate)
        offset += 4
        #magnetic_field_components = struct.unpack_from(">fff", data, offset)
        #row2.append(magnetic_field_components)
        offset += 12
        #proton_gyrofrequency = struct.unpack_from(">f", data, offset)[0]
        #row2.append(proton_gyrofrequency)
        offset += 4
        #solar_position_x = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #solar_position_y = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #solar_position_z = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #row2.append(f"({solar_position_x},{solar_position_y},{solar_position_z})")
        #software_component_version = struct.unpack_from(">B", data, offset)[0]
        #row2.append(software_component_version)
        offset += 1
        #software_component_sub_version = struct.unpack_from(">B", data, offset)[0]
        #row2.append(software_component_sub_version)
        offset += 1

        # Attitude Parameters
        #matrix_msat2geo_11 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_12 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_13 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_21 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_22 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_23 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_31 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_32 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_msat2geo_33 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #row2.append(f"(({matrix_msat2geo_11},{matrix_msat2geo_12},{matrix_msat2geo_13}),({matrix_msat2geo_21},{matrix_msat2geo_22},{matrix_msat2geo_23}),({matrix_msat2geo_31},{matrix_msat2geo_32},{matrix_msat2geo_33}))")
        #matrix_mgeo2lgm_11 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_12 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_13 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_21 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_22 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_23 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_31 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_32 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #matrix_mgeo2lgm_33 = struct.unpack_from(">f", data, offset)[0]
        offset += 4
        #row2.append(f"(({matrix_mgeo2lgm_11},{matrix_mgeo2lgm_12},{matrix_mgeo2lgm_13}),({matrix_mgeo2lgm_21},{matrix_mgeo2lgm_22},{matrix_mgeo2lgm_23}),({matrix_mgeo2lgm_31},{matrix_mgeo2lgm_32},{matrix_mgeo2lgm_33}))")
        #quality_index = struct.unpack_from(">H", data, offset)[0]
        #row2.append(quality_index)
        offset += 2
        #software_version_number = struct.unpack_from(">B", data, offset)[0]
        #row2.append(software_version_number)
        offset += 1
        #software_sub_version_number = struct.unpack_from(">B", data, offset)[0]
        #row2.append(software_sub_version_number)
        offset += 1

        if apid == "1129":
          # Data header
          data_type = struct.unpack_from("21s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 21
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          data_coordinate_system = struct.unpack_from("9s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_coordinate_system)
          offset += 9
          matrix_sen_to_sat = []
          for i in range(9):
            matrix_sen_to_sat.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          matrix_sen_to_sat = ";".join(map(str, matrix_sen_to_sat))
          row2.append(matrix_sen_to_sat)
          data_unit = struct.unpack_from("16s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_unit)
          offset += 16
          sampling_frequency = struct.unpack_from(">f", data, offset)[0]
          row2.append(sampling_frequency)
          offset += 4
          sample_data_num_per_component = struct.unpack_from(">H", data, offset)[0]
          row2.append(sample_data_num_per_component)
          offset += 2
          time_duration_of_one_data_array = struct.unpack_from(">f", data, offset)[0]
          row2.append(time_duration_of_one_data_array)
          offset += 4
          # First component waveform
          first_component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(first_component_name)
          offset += 3
          waveform_sample_array_first_component = []
          for i in range(256):
            waveform_sample_array_first_component.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          waveform_sample_array_first_component = ";".join(map(str, waveform_sample_array_first_component))
          row2.append(waveform_sample_array_first_component)
          # Second component waveform
          second_component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(second_component_name)
          offset += 3
          waveform_sample_array_second_component = []
          for i in range(256):
            waveform_sample_array_second_component.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          waveform_sample_array_second_component = ";".join(map(str, waveform_sample_array_second_component))
          row2.append(waveform_sample_array_second_component)
          # Third component waveform
          third_component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(third_component_name)
          offset += 3
          waveform_sample_array_third_component = []
          for i in range(256):
            waveform_sample_array_third_component.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          waveform_sample_array_third_component = ";".join(map(str, waveform_sample_array_third_component))
          row2.append(waveform_sample_array_third_component)
          # Probe E1 sensor potential
          probe_1_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(probe_1_name)
          offset += 3
          potential_array_e1_probe = []
          for i in range(256):
            potential_array_e1_probe.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          potential_array_e1_probe = ";".join(map(str, potential_array_e1_probe))
          row2.append(potential_array_e1_probe)
          # Probe E2 sensor potential
          probe_2_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(probe_2_name)
          offset += 3
          potential_array_e2_probe = []
          for i in range(256):
            potential_array_e2_probe.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          potential_array_e2_probe = ";".join(map(str, potential_array_e2_probe))
          row2.append(potential_array_e2_probe)
          # Probe E3 sensor potential
          probe_3_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(probe_3_name)
          offset += 3
          potential_array_e3_probe = []
          for i in range(256):
            potential_array_e3_probe.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          potential_array_e3_probe = ";".join(map(str, potential_array_e3_probe))
          row2.append(potential_array_e3_probe)
          # Probe E4 sensor potential
          probe_4_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(probe_4_name)
          offset += 3
          potential_array_e4_probe = []
          for i in range(256):
            potential_array_e4_probe.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          potential_array_e4_probe = ";".join(map(str, potential_array_e4_probe))
          row2.append(potential_array_e4_probe)

        if apid == "1130" or apid == "1135":
          # Data header
          data_type = struct.unpack_from("21s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 21
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          data_coordinate_system = struct.unpack_from("9s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_coordinate_system)
          offset += 9
          matrix_sen_to_sat = []
          for i in range(9):
            matrix_sen_to_sat.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          matrix_sen_to_sat = ";".join(map(str, matrix_sen_to_sat))
          row2.append(matrix_sen_to_sat)
          data_unit = struct.unpack_from("16s", data, offset)[0].decode('windows-1251').strip()
          data_unit = data_unit.replace('µ', 'u')  # символа µ нет в кодировке utf-8 
          row2.append(data_unit)
          offset += 16
          sampling_frequency = struct.unpack_from(">f", data, offset)[0]
          row2.append(sampling_frequency)
          offset += 4
          sample_data_num_per_component = struct.unpack_from(">H", data, offset)[0]
          row2.append(sample_data_num_per_component)
          offset += 2
          time_duration_of_one_data_array = struct.unpack_from(">f", data, offset)[0]
          row2.append(time_duration_of_one_data_array)
          offset += 4
          # First component waveform
          first_component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(first_component_name)
          offset += 3
          waveform_sample_array_first_component = []
          for i in range(4096):
            waveform_sample_array_first_component.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          waveform_sample_array_first_component = ";".join(map(str, waveform_sample_array_first_component))
          row2.append(waveform_sample_array_first_component)
          # Second component waveform
          second_component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(second_component_name)
          offset += 3
          waveform_sample_array_second_component = []
          for i in range(4096):
            waveform_sample_array_second_component.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          waveform_sample_array_second_component = ";".join(map(str, waveform_sample_array_second_component))
          row2.append(waveform_sample_array_second_component)
          # Third component waveform
          third_component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(third_component_name)
          offset += 3
          waveform_sample_array_third_component = []
          for i in range(4096):
            waveform_sample_array_third_component.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          waveform_sample_array_third_component = ";".join(map(str, waveform_sample_array_third_component))
          row2.append(waveform_sample_array_third_component)

        if apid == "1131" or apid == "1133" or apid == "1136":
          # Data header
          data_type = struct.unpack_from("21s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 21
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          data_coordinate_system = struct.unpack_from("9s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_coordinate_system)
          offset += 9
          data_unit = struct.unpack_from("16s", data, offset)[0].decode('windows-1251').strip()
          data_unit = data_unit.replace('µ', 'u')  # символа µ нет в кодировке utf-8 
          row2.append(data_unit)
          offset += 16
          sampling_frequency = struct.unpack_from(">f", data, offset)[0]
          row2.append(sampling_frequency)
          offset += 4
          sample_data_num_per_component = struct.unpack_from(">H", data, offset)[0]
          row2.append(sample_data_num_per_component)
          offset += 2
          time_duration_of_one_data_array = struct.unpack_from(">f", data, offset)[0]
          row2.append(time_duration_of_one_data_array)
          offset += 4
          #Waveform data
          component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(component_name)
          offset += 3
          waveform_sample_array = []
          for i in range(8192):
            waveform_sample_array.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          waveform_sample_array = ";".join(map(str, waveform_sample_array))
          row2.append(waveform_sample_array)

        if apid == "1132" or apid == "1134" or apid == "1137":
          # Data header
          data_type = struct.unpack_from("21s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 21
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          data_coordinate_system = struct.unpack_from("9s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_coordinate_system)
          offset += 9
          component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
          row2.append(component_name)
          offset += 3
          data_unit = struct.unpack_from("16s", data, offset)[0].decode('windows-1251').strip()
          data_unit = data_unit.replace('µ', 'u')  # символа µ нет в кодировке utf-8 
          row2.append(data_unit)
          offset += 16
          Nb = struct.unpack_from(">B", data, offset)[0]
          row2.append(Nb)
          offset += 1
          Nbf = struct.unpack_from(">H", data, offset)[0]
          row2.append(Nbf)
          offset += 2
          total_time_duration_of_Nb_spectra = struct.unpack_from(">f", data, offset)[0]
          row2.append(total_time_duration_of_Nb_spectra)
          offset += 4
          frequency_resolution = struct.unpack_from(">f", data, offset)[0]
          row2.append(frequency_resolution)
          offset += 4
          frequency_range = []
          for i in range(2):
            frequency_range.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          frequency_range = "-".join(map(str, frequency_range))
          row2.append(frequency_range)
          ut_year = struct.unpack_from(">H", data, offset)[0]
          offset += 2
          ut_month = struct.unpack_from(">H", data, offset)[0]
          offset += 2
          ut_day = struct.unpack_from(">H", data, offset)[0]
          offset += 2
          ut_hour = struct.unpack_from(">H", data, offset)[0]
          offset += 2
          ut_minute = struct.unpack_from(">H", data, offset)[0]
          offset += 2
          ut_second = struct.unpack_from(">H", data, offset)[0]
          offset += 2
          ut_millisecond = struct.unpack_from(">H", data, offset)[0]
          offset += 2
          row2.append(f"{ut_year}-{ut_month}-{ut_day}-{ut_hour}-{ut_minute}-{ut_second}-{ut_millisecond}")
          # Power spectrum data
          row1_1134_add = []
          for nb in range(1, Nb + 1):
            if (f"Power array of the {nb} spectrum") not in row1_1134_add:
              row1_1134_add.append(f"Power array of the {nb} spectrum")
            power_array = []
            for nbf in range(Nbf):
              power_array.append(struct.unpack_from(">f", data, offset)[0])
              offset += 4
            power_array = ";".join(map(str, power_array))
            row2.append(power_array)

        if (apid == "1138"):
          # Data header
          data_type = struct.unpack_from("21s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 21
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          data_sub_type = struct.unpack_from(">B", data, offset)[0]
          row2.append(data_sub_type)
          offset += 1
          if data_sub_type == 0:
            row1_1138_add = [
              "Study title",
              "Component name",
              "Time resolution",
              "Class number (Nbclasses)",
              "Number of spectra (Nbs)",
              #"0",
              "Unit name for the class ranges",
              "Minimum ranges for the classes Di",
              "Maximum ranges for the classes Di",
              "Spectrum validity",
              "Nbs vectors of Nbclasses (Spectrogram intensity)",
              "Nbs vectors of Nbclasses (Spectrogram uncertainty)"
            ]
            study_title = struct.unpack_from("20s", data, offset)[0].decode('windows-1251').strip()
            row2.append(study_title)
            offset += 20
            component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
            row2.append(component_name)
            offset += 3
            time_resolution = struct.unpack_from(">f", data, offset)[0]
            row2.append(time_resolution)
            offset += 4
            class_number = struct.unpack_from(">B", data, offset)[0]
            row2.append(class_number)
            offset += 1
            Nbs = struct.unpack_from(">B", data, offset)[0]
            row2.append(Nbs)
            offset += 1
            offset += 1
            # Class description
            unit_name_class_ranges = struct.unpack_from("20s", data, offset)[0].decode('windows-1251').strip()
            row2.append(unit_name_class_ranges)
            offset += 10
            min_ranges_classes = []
            for i in range(20):
              min_ranges_classes.append(struct.unpack_from(">f", data, offset)[0])
              offset += 4
            min_ranges_classes = ";".join(map(str, min_ranges_classes))
            row2.append(min_ranges_classes)
            max_ranges_classes = []
            for i in range(20):
              max_ranges_classes.append(struct.unpack_from(">f", data, offset)[0])
              offset += 4
            max_ranges_classes = ";".join(map(str, max_ranges_classes))
            row2.append(max_ranges_classes)
            # Spectrogram intensity
            spectrum_validity = []
            for i in range(128):
              spectrum_validity.append(struct.unpack_from(">B", data, offset)[0])
              offset += 1
            spectrum_validity = ";".join(map(str, spectrum_validity))
            row2.append(spectrum_validity)
            Nbs_vectors_of_Nbclasses_1 = []
            for row in range(128):
              row_data = []
              for col in range(20):
                row_data.append(str(struct.unpack_from(">B", data, offset)[0]))
                offset += 1
              Nbs_vectors_of_Nbclasses_1.append(";".join(row_data))
            Nbs_vectors_of_Nbclasses_1 = "|".join(Nbs_vectors_of_Nbclasses_1)
            row2.append(Nbs_vectors_of_Nbclasses_1) 
            # Spectrogram uncertainty
            Nbs_vectors_of_Nbclasses_2 = []
            for row in range(128):
              row_data = []
              for col in range(20):
                row_data.append(str(struct.unpack_from(">B", data, offset)[0]))
                offset += 1
              Nbs_vectors_of_Nbclasses_2.append(";".join(row_data))
            Nbs_vectors_of_Nbclasses_2 = "|".join(Nbs_vectors_of_Nbclasses_2)
            row2.append(Nbs_vectors_of_Nbclasses_2)
          elif data_sub_type == 1:
            row1_1138_add = [
              "Study title",
              "Component name",
              "Time resolution",
              "Class number (Nbclasses)",
              "Number of plot points (Nbp)",
              "Number of curves (Nbc)",
              "Unit name for the class ranges",
              "Minimum ranges for the classes Di",
              "Maximum ranges for the classes Di",
              "Spectrum validity",
              "Nbc vectors of Nbp elements (Spectrogram intensity)",
              "Nbs vectors of Nbp elements (Spectrogram uncertainty)"
            ]
            study_title = struct.unpack_from("20s", data, offset)[0].decode('windows-1251').strip()
            row2.append(study_title)
            offset += 20
            component_name = struct.unpack_from("3s", data, offset)[0].decode('windows-1251').strip()
            row2.append(component_name)
            offset += 3
            time_resolution = struct.unpack_from(">f", data, offset)[0]
            row2.append(time_resolution)
            offset += 4
            class_number = struct.unpack_from(">B", data, offset)[0]
            row2.append(class_number)
            offset += 1
            Nbp = struct.unpack_from(">B", data, offset)[0]
            row2.append(Nbp)
            offset += 1
            Nbc = struct.unpack_from(">B", data, offset)[0]
            row2.append(Nbc)
            offset += 1
            # Class description
            unit_name_class_ranges = struct.unpack_from("20s", data, offset)[0].decode('windows-1251').strip()
            row2.append(unit_name_class_ranges)
            offset += 10
            min_ranges_classes = []
            for i in range(20):
              min_ranges_classes.append(struct.unpack_from(">f", data, offset)[0])
              offset += 4
            min_ranges_classes = ";".join(map(str, min_ranges_classes))
            row2.append(min_ranges_classes)
            max_ranges_classes = []
            for i in range(20):
              max_ranges_classes.append(struct.unpack_from(">f", data, offset)[0])
              offset += 4
            max_ranges_classes = ";".join(map(str, max_ranges_classes))
            row2.append(max_ranges_classes)
            # Spectrogram intensity
            spectrum_validity = []
            for i in range(128):
              spectrum_validity.append(struct.unpack_from(">B", data, offset)[0])
              offset += 1
            spectrum_validity = ";".join(map(str, spectrum_validity))
            row2.append(spectrum_validity)
            Nbc_vectors_of_Nbp_classes_1 = []
            for row in range(128):
              row_data = []
              for col in range(20):
                row_data.append(str(struct.unpack_from(">B", data, offset)[0]))
                offset += 1
              Nbc_vectors_of_Nbp_classes_1.append(";".join(row_data))
            Nbc_vectors_of_Nbp_classes_1 = "|".join(Nbc_vectors_of_Nbp_classes_1)
            row2.append(Nbc_vectors_of_Nbp_classes_1) 
            # Spectrogram uncertainty
            Nbc_vectors_of_Nbp_classes_2 = []
            for row in range(128):
              row_data = []
              for col in range(20):
                row_data.append(str(struct.unpack_from(">B", data, offset)[0]))
                offset += 1
              Nbc_vectors_of_Nbp_classes_2.append(";".join(row_data))
            Nbc_vectors_of_Nbp_classes_2 = "|".join(Nbc_vectors_of_Nbp_classes_2)
            row2.append(Nbc_vectors_of_Nbp_classes_2)

        if (apid == "1139" or apid == "1140"):
          # Data header
          data_type = struct.unpack_from("10s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 10
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          time_resolution = struct.unpack_from(">f", data, offset)[0]
          row2.append(time_resolution)
          offset += 4
          density_unit = struct.unpack_from("6s", data, offset)[0].decode('windows-1251').strip()
          row2.append(density_unit)
          offset += 6
          temperature_unit = struct.unpack_from("6s", data, offset)[0].decode('windows-1251').strip()
          row2.append(temperature_unit)
          offset += 6
          velocity_unit = struct.unpack_from("6s", data, offset)[0].decode('windows-1251').strip()
          row2.append(velocity_unit)
          offset += 6
          potential_unit = struct.unpack_from("6s", data, offset)[0].decode('windows-1251').strip()
          row2.append(potential_unit)
          offset += 6
          angle_unit = struct.unpack_from("6s", data, offset)[0].decode('windows-1251').strip()
          row2.append(angle_unit)
          offset += 6
          # Density and temperature
          h_density = struct.unpack_from(">f", data, offset)[0]
          row2.append(h_density)
          offset += 4
          he_density = struct.unpack_from(">f", data, offset)[0]
          row2.append(he_density)
          offset += 4
          o_density = struct.unpack_from(">f", data, offset)[0]
          row2.append(he_density)
          offset += 4
          ions_temperature = struct.unpack_from(">f", data, offset)[0]
          row2.append(ions_temperature)
          offset += 4
          # Plasma velocity
          ions_velocity_Oz = struct.unpack_from(">f", data, offset)[0]
          row2.append(ions_velocity_Oz)
          offset += 4
          ion_velocity_angle_Oz = struct.unpack_from(">f", data, offset)[0]
          row2.append(ion_velocity_angle_Oz)
          offset += 4
          ion_velocity_projection_angle_OxOy = struct.unpack_from(">f", data, offset)[0]
          row2.append(ion_velocity_projection_angle_OxOy)
          offset += 4
          # Satellite potential
          satellite_potential = struct.unpack_from(">f", data, offset)[0]
          row2.append(satellite_potential)
          offset += 4

        if (apid == "1141"):
          # Data header
          data_type = struct.unpack_from("10s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 10
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          time_resolution = struct.unpack_from(">f", data, offset)[0]
          row2.append(time_resolution)
          offset += 4
          polarisation_voltage = struct.unpack_from(">f", data, offset)[0]
          row2.append(polarisation_voltage)
          offset += 4
          descrimination_level = struct.unpack_from(">f", data, offset)[0]
          row2.append(descrimination_level)
          offset += 4
          spectum_data_unit = struct.unpack_from("20s", data, offset)[0].decode('windows-1251').strip()
          row2.append(spectum_data_unit)
          offset += 20
          pitch_angle_unit = struct.unpack_from("6s", data, offset)[0].decode('windows-1251').strip()
          row2.append(pitch_angle_unit)
          offset += 6
          # Electron spectra
          spectrum1 = []
          for i in range(256):
            spectrum1.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum1 = ";".join(map(str, spectrum1))
          row2.append(spectrum1)
          spectrum2 = []
          for i in range(256):
            spectrum2.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum2 = ";".join(map(str, spectrum2))
          row2.append(spectrum2)
          spectrum3 = []
          for i in range(256):
            spectrum3.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum3 = ";".join(map(str, spectrum3))
          row2.append(spectrum3)
          spectrum4 = []
          for i in range(256):
            spectrum4.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum4 = ";".join(map(str, spectrum4))
          row2.append(spectrum4)
          # Energy table
          energy_table = []
          for i in range(256):
            energy_table.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          energy_table = ";".join(map(str, energy_table))
          row2.append(energy_table)
          # Pitch angle data
          pitch_angle = struct.unpack_from(">f", data, offset)[0]
          row2.append(pitch_angle)
          offset += 4

        if (apid == "1142"):
          # Data header
          data_type = struct.unpack_from("10s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 10
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          spectrum_time_resolution = struct.unpack_from(">f", data, offset)[0]
          row2.append(spectrum_time_resolution)
          offset += 4
          counters_time_resolution = struct.unpack_from(">f", data, offset)[0]
          row2.append(counters_time_resolution)
          offset += 4
          polarisation_voltage = struct.unpack_from(">f", data, offset)[0]
          row2.append(polarisation_voltage)
          offset += 4
          descrimination_level = struct.unpack_from(">f", data, offset)[0]
          row2.append(descrimination_level)
          offset += 4
          threshold_low_interval_1 = struct.unpack_from(">f", data, offset)[0]
          row2.append(threshold_low_interval_1)
          offset += 4
          threshold_low_interval_2 = struct.unpack_from(">f", data, offset)[0]
          row2.append(threshold_low_interval_2)
          offset += 4
          threshold_low_interval_3 = struct.unpack_from(">f", data, offset)[0]
          row2.append(threshold_low_interval_3)
          offset += 4
          threshold_high_interval_3 = struct.unpack_from(">f", data, offset)[0]
          row2.append(threshold_high_interval_3)
          offset += 4
          spectum_data_unit = struct.unpack_from("20s", data, offset)[0].decode('windows-1251').strip()
          row2.append(spectum_data_unit)
          offset += 20
          pitch_angle_unit = struct.unpack_from("6s", data, offset)[0].decode('windows-1251').strip()
          row2.append(pitch_angle_unit)
          offset += 6
          # Counters and spectrum data
          counters1 = []
          for i in range(12):
            counters1.append(struct.unpack_from(">i", data, offset)[0])
            offset += 4
          counters1 = ";".join(map(str, counters1))
          row2.append(counters1)
          spectrum1 = []
          for i in range(128):
            spectrum1.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum1 = ";".join(map(str, spectrum1))
          row2.append(spectrum1)
          counters2 = []
          for i in range(12):
            counters2.append(struct.unpack_from(">i", data, offset)[0])
            offset += 4
          counters2 = ";".join(map(str, counters2))
          row2.append(counters2)
          spectrum2 = []
          for i in range(128):
            spectrum2.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum2 = ";".join(map(str, spectrum2))
          counters3 = []
          for i in range(12):
            counters3.append(struct.unpack_from(">i", data, offset)[0])
            offset += 4
          counters3 = ";".join(map(str, counters3))
          row2.append(counters3)
          spectrum3 = []
          for i in range(128):
            spectrum3.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum3 = ";".join(map(str, spectrum3))
          row2.append(spectrum3)
          counters4 = []
          for i in range(12):
            counters4.append(struct.unpack_from(">i", data, offset)[0])
            offset += 4
          counters4 = ";".join(map(str, counters4))
          row2.append(counters4)
          spectrum4 = []
          for i in range(128):
            spectrum4.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum4 = ";".join(map(str, spectrum4))
          row2.append(spectrum4)
          counters5 = []
          for i in range(12):
            counters5.append(struct.unpack_from(">i", data, offset)[0])
            offset += 4
          counters5 = ";".join(map(str, counters5))
          row2.append(counters5)
          spectrum5 = []
          for i in range(128):
            spectrum5.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum5 = ";".join(map(str, spectrum5))
          row2.append(spectrum5)
          counters6 = []
          for i in range(12):
            counters6.append(struct.unpack_from(">i", data, offset)[0])
            offset += 4
          counters6 = ";".join(map(str, counters6))
          row2.append(counters6)
          spectrum6 = []
          for i in range(128):
            spectrum6.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum6 = ";".join(map(str, spectrum6))
          row2.append(spectrum6)
          counters7 = []
          for i in range(12):
            counters7.append(struct.unpack_from(">i", data, offset)[0])
            offset += 4
          counters7 = ";".join(map(str, counters7))
          row2.append(counters7)
          spectrum7 = []
          for i in range(128):
            spectrum7.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          spectrum7 = ";".join(map(str, spectrum7))
          row2.append(spectrum7)
          # Energy table
          energy_table = []
          for i in range(128):
            energy_table.append(struct.unpack_from(">f", data, offset)[0])
            offset += 4
          energy_table = ";".join(map(str, energy_table))
          row2.append(energy_table)
          # Pitch angle data
          pitch_angle = struct.unpack_from(">f", data, offset)[0]
          row2.append(pitch_angle)
          offset += 4

        if (apid == "1143" or apid == "1144"):
          # Data header
          data_type = struct.unpack_from("10s", data, offset)[0].decode('windows-1251').strip()
          row2.append(data_type)
          offset += 10
          #house_keepings = struct.unpack_from(">32B", data, offset)
          #row2.append(house_keepings)
          offset += 32
          time_resolution = struct.unpack_from(">f", data, offset)[0]
          row2.append(time_resolution)
          offset += 4
          density_unit = struct.unpack_from("5s", data, offset)[0].decode('windows-1251').strip()
          row2.append(density_unit)
          offset += 5
          temperature_unit = struct.unpack_from("5s", data, offset)[0].decode('windows-1251').strip()
          row2.append(temperature_unit)
          offset += 5
          potential_unit = struct.unpack_from("5s", data, offset)[0].decode('windows-1251').strip()
          row2.append(potential_unit)
          offset += 5
          # Plasma parameters
          electron_density = struct.unpack_from(">f", data, offset)[0]
          row2.append(electron_density)
          offset += 4
          ion_density = struct.unpack_from(">f", data, offset)[0]
          row2.append(ion_density)
          offset += 4
          electron_temperature = struct.unpack_from(">f", data, offset)[0]
          row2.append(electron_temperature)
          offset += 4
          plasma_potential = struct.unpack_from(">f", data, offset)[0]
          row2.append(plasma_potential)
          offset += 4
          floating_potential = struct.unpack_from(">f", data, offset)[0]
          row2.append(floating_potential)
          offset += 4
          satellite_potential = struct.unpack_from(">f", data, offset)[0]
          row2.append(satellite_potential)
          offset += 4
        csvwriter.writerow(row2)
        row_count += 1
        row2 = []

  if apid == "1132" or apid == "1134" or apid == "1137":
    with open(output_file, "r") as file:
      rows = list(csv.reader(file))  # Считываем все строки
    rows[0] += row1_1134_add  # Дополняем первую строку
    with open(output_file, "w", newline="") as file:
      csv.writer(file).writerows(rows)  # Перезаписываем файл
  elif apid == "1138":
    with open(output_file, "r") as file:
      rows = list(csv.reader(file))
    rows[0] += row1_1138_add
    with open(output_file, "w", newline="") as file:
      csv.writer(file).writerows(rows)

  print(f"Готово! Файл сохранён как {output_file}")
  #from google.colab import files
  #files.download(output_file)

file_path = input("Введите путь к файлу .DAT: ")
while not os.path.isfile(file_path): # Проверка существует ли файл
    print("Ошибка: файл не найден! Попробуйте снова.")
    file_path = input("Введите путь к файлу .DAT: ")
read_dat_file_to_csv(file_path)