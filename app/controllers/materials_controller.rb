class MaterialsController < ApplicationController
    def index
        @materials = Material.all
    end
    
    def create
        @material = Material.new(material_params)

        if @material.save
        redirect_to @material
        else
            render 'new'
        end
    end
    
    def new
        @containers = Container.all
    end

    def edit
    end

    def show
        @material = Material.find(params[:id])
    end

    def update
    end
    
    def destroy
        @material = Material.find(params[:id])
        @material.destroy
 
    redirect_to materials_path
    end
    
    private
        def material_params
            params.require(:material).permit(:name, :container_id)
        end
end
