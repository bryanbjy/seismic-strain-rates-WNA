gmt pscoast -R-125/-113/31/39.5 -JM6i -B2 -W0.5 -Ggrey -N1 -N2 -Dl -A5000 -K -P >vel_big_SA.ps
gmt psvelo vel_platemotion.txt -R -JM -W0.5,red -Se0.02/1/15 -Gred -O -K >> vel_big_SA.ps
gmt pslegend -R -JM -Dx0i/0i/2i/BL -O -K << EOF >> vel_big_SA.ps
S 0.5i v0.07i+a60+e+p1.5p,red 0.5i red 0.5p 0.8i 50mmyr^-1
EOF

gmt pstext -R -JM << END -F+f11p,Helvetica-Bold -O -K >> vel_big_SA.ps
-127.5 46 JDF
-120 45 NA
-128 37 PA
-129 50 EXP
END

gmt pstext -R -JM << END -F+f10p,Helvetica -O -K >> vel_big_SA.ps
-122 52 BC
-119 47.5 WA
-121 44 OR
-121.5 39 CA
-117 40 NV
-115.5 45 ID
END

gmt psxy bird_plates.xy -R -JM -W1.0,purple -O -K >> vel_big_SA.ps

gs vel_big_SA.ps