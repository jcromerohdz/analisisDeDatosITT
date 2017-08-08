graph [
  node [
    id 0
    label "Ray"
    edad 27
  ]
  node [
    id 1
    label "Rene"
    edad 32
  ]
  node [
    	id 2
    	label "Chris"
    	edad 38
  	]
  node [
    	id 3
    	label "Arnulfo"
    	edad 27
  	]
  node [
	id 4
	label "Adolfo"
	edad 39
  	]
  node [
        id 5
        label "Alfredo"
        edad 25
  	]
  node [
        id 6
        label "Gaby"
        edad 40
        ]
 edge [
        source 6
        target 0
        ]
 edge [
	source 0
	target 1
 	]
 edge [
	source 1
	target 2
 	]
 edge [ 
	source 2 
	target 3
 	] 
edge [ 
	source 3 
	target 4 
	] 
edge [
        source 5
        target 2
        ]

]
