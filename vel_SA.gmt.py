gmt pscoast -R-125/-113/31/39.5 -JM6i -B2 -W0.5 -Ggrey -N1 -N2 -Dl -A5000 -K -P >vel_SA.ps
gmt psvelo vel_compare.txt -R -JM -W0.75,red,dashed -Se0.05/1/15 -Gred -O -K >> vel_SA.ps
gmt psvelo vel_calculate.txt -R -JM -W0.5,black -Se0.05/1/15 -Gblack -O -K >> vel_SA.ps
gmt pslegend -R -JM -Dx0i/0i/2i/BL -F -O -K << EOF >> vel_SA.ps
H 12 Times-Bold Velocity Vectors mmyr^-1
S 0.5i v0.1i+e+p1.0p 0.8i black 0.5p 1i calculated
S 0.5i v0.1i+e+p1.0p,red,dashed 0.8i red 0.5p 1i geodetic
EOF

gmt pstext -R -JM << END -F+f11p,Helvetica-Bold -O -K >> vel_SA.ps
-127.5 46 JDF
-120 45 NA
-128 37 PA
-129 50 EXP
END

gmt pstext -R -JM << END -F+f10p,Helvetica -O -K >> vel_SA.ps
-122 52 BC
-119 47.5 WA
-121 44 OR
-121.5 39 CA
-117 40 NV
-115.5 45 ID
END

gmt psxy bird_plates.xy -R -JM -W1.0,purple -O -K >> vel_SA.ps

gmt psxy <<END -Frrefpoint -R -JM -W2 -O>> vel_SA.ps
>Box 1
-115 32.5 
-117 32.5
-117.5 34.5
-116 35.5
-115 32.5
>Box 2
-120.5 33.2 
-117.5 33.7
-117.5 34.5
-120.5 35.0
-120.5 33.2
>Box 3
-121.7 35.2
-119 34.8
-118.5 35.4 
-120.8 36.9
-121.7 36.2
-121.7 35.2
>Box 4
-118.4 35.7
-117.5 35.7
-115.8 37
-117.1 38
-117.9 37.1
-118.8 36.9
-118.4 35.7
>Box 5
-122.4 36.2
-121 37.1
-121.8 38.9
-123.7 38
-122.4 36.2
>Box 6
-120 37
-118.9 37
-117.8 37.2
-117.6 38.1
-119.2 39.1
-120.7 38.8
-120 37
>Box 7
-127.6 40.2
-124.6 39.95
-124.5 40.6
-127.4 40.7
-127.6 40.2
>Box 8
-127.4 40.7
-124.65 40.6
-126.3 42.9
-127.4 40.7
>Box 9
-128.9 40.8
-127.6 40.2
-126.5 42.65
-127.5 42.75
-128.9 40.8
>Box 10
-129.05 43.2
-126.7 42.7
-126.4 43
-128.2 43.9
-129.05 43.2
>Box 11
-128.65 43.7
-128.60 43.95
-129 44.1
-129.2 43.8
-128.65 43.7
>Box 12
-129.25 43.85
-129.2 44.2
-130.35 44.55
-130.3 44.1
-129.25 43.85
>Box 11
-129.85 50.4
-131.4 49.9
-129.2 47.95
-128.05 47.9
-129.85 50.4
>Box 12
-128.2 48.3
-127.4 49
-128.3 50
-129.3 49.7
-128.2 48.3
>Box 13
-127.3 49
-126.5 49.4
-127.3 50.1
-128.05 49.8
-127.3 49
>Box 14
-130.8 50.1
-129.1 50.6
-130.8 52.1
-132.15 51.8
-130.8 50.1
>Box 15
-132.1 51.8
-131 52.4
-131.9 53.0
-133.7 52.95
-132.1 51.8
END


gs vel_SA.ps