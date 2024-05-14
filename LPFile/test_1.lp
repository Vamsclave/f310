Minimize
   z: 1 quantity_e_0_2_0 + 1 quantity_e_1_2_0 + 1 quantity_e_3_4_0 + 1 quantity_e_3_5_0 + 1 quantity_e_2_3_0 + 1 quantity_e_0_2_1 + 1 quantity_e_1_2_1 + 1 quantity_e_3_4_1 + 1 quantity_e_3_5_1 + 1 quantity_e_2_3_1
Subject to
   contraite_4_0: quantity_e_3_4_0  = 10
   contraite_5_0: quantity_e_3_5_0  = 5
   contraite_4_1: quantity_e_3_4_1  = 30
   contraite_5_1: quantity_e_3_5_1  = 5
   contraite_0_0: quantity_e_0_2_0  <= 10
   contraite_1_0: quantity_e_1_2_0  <= 5
   contraite_0_1: quantity_e_0_2_1  <= 20
   contraite_1_1: quantity_e_1_2_1  <= 15
   contraite_2_0: quantity_e_0_2_0 + quantity_e_1_2_0 - quantity_e_2_3_0 = 0
   contraite_3_0: quantity_e_2_3_0 - quantity_e_3_4_0 - quantity_e_3_5_0 = 0
   contraite_2_1: quantity_e_0_2_1 + quantity_e_1_2_1 - quantity_e_2_3_1 = 0
   contraite_3_1: quantity_e_2_3_1 - quantity_e_3_4_1 - quantity_e_3_5_1 = 0
Integer
   quantity_e_0_2_0
   quantity_e_1_2_0
   quantity_e_3_4_0
   quantity_e_3_5_0
   quantity_e_2_3_0
   quantity_e_0_2_1
   quantity_e_1_2_1
   quantity_e_3_4_1
   quantity_e_3_5_1
   quantity_e_2_3_1
End