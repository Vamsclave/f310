Minimize
   z: 1 quantity_e_0_0 + 1 quantity_e_1_0 + 1 quantity_e_2_0 + 1 quantity_e_3_0 + 1 quantity_e_4_0
Subject to
   contraite_4_0: quantity_e_2_0  = 40
   contraite_5_0: quantity_e_3_0  = 10
   contraite_0_0: quantity_e_0_0  <= 30
   contraite_1_0: quantity_e_1_0  <= 20
   contraite_2_0: quantity_e_0_0 + quantity_e_1_0 - quantity_e_4_0 = 0
   contraite_3_0: quantity_e_4_0 - quantity_e_2_0 - quantity_e_3_0 = 0
Bounds
   quantity_e_0_0 >= 0
   quantity_e_1_0 >= 0
   quantity_e_2_0 >= 0
   quantity_e_3_0 >= 0
   quantity_e_4_0 >= 0
Integer
   quantity_e_0_0
   quantity_e_1_0
   quantity_e_2_0
   quantity_e_3_0
   quantity_e_4_0
End