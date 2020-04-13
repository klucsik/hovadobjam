class OnamesController < ApplicationController

    def index
    end
    
    def create
        @item = Item.find(params[:item_id])
        @oname = @item.onames.create(onames_params)
        redirect_to item_path(@item)
    end
    
    def new
    end

    def edit
    end

    def show
    end

    def update
    end
    
    def destroy
    end
    
    private
        def onames_params
            params.require(:oname).permit(:name)
        end
end
