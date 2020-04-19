class ContainersController < ApplicationController
    def index
        @containers = Container.all
    end
    
    def create
        @container = Container.new(container_params)

        if @container.save
        redirect_to containers_path
        else
            render 'new'
        end
    end
    
    def new
    end

    def edit
    end

    def show
        @container = Container.find(params[:id])
    end

    def update
    end
    
    def destroy
        @container =  Container.find(params[:id])
        @container.destroy
 
    redirect_to containers_path
    end
    
    private
        def container_params
            params.require(:container).permit(:name)
        end
end
