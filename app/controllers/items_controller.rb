class ItemsController < ApplicationController

    def index
        @items = Item.all
    end
    
    def create
        @item = Item.new(item_params)

        if @item.save
        redirect_to @item
        else
            render 'new'
        end
    end
    
    def new
        @item = Item.new
    end

    def edit
    end

    def show
        @item = Item.find(params[:id])
    end

    def update
    end
    
    def destroy
        @item = Item.find(params[:id])
        @item.destroy
 
    redirect_to items_path
    end
    
    private
        def item_params
            params.require(:item).permit(:name, :material_id)
        end
end
