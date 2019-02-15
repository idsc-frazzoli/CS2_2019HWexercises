connect-%: 
	bash -c "docker -H $*.local run -it --net host --privileged -v /data:/data --name exercises lapandic/rpi-duckiebot-cs2:latest"
	bash -c "docker -H $*.local start exercises"
	bash -c "docker -H $*.local exec -it exercises /bin/bash"

copy-to-%: 
	bash -c "docker -H $*.local cp ~/CSII exercises:/home/software/"

copy-from-%: 
	bash -c "docker -H $*.local cp exercises:/home/software/CSII ~/"

change-trim-%: 
	bash -c "docker -H $*.local exec -it exercises bash -c 'source /home/software/docker/env.sh && rosservice call /$*/inverse_kinematics_node/set_trim -- $(trim)'"
	@echo "Changed trim for $* to $(trim)"
