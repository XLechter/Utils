function [] = convertply2obj(inputdir, sphere_size)



outputdir = [ inputdir  ]

if ~exist(outputdir, 'dir')
	mkdir(outputdir)
end

if isempty(sphere_size)
    sphere_size = 0.015
end

fileList = dir(  [inputdir '/*pc.ply' ]) ;

numfiles = size( fileList,1 )

for i=1:numfiles
i
	fname = [inputdir '/' fileList(i).name ]
	targetname = [outputdir '/'  fileList(i).name(1:end-4) '.obj' ]
	
	
	pointcloud2sphere( fname ,   targetname,   sphere_size ) ;
	
	
end
	
	
	
	