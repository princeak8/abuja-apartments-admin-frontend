<template>
    <div class="w-full">
        <Navbar />
        <div class="flex flex-row w-full border-1 border-blue-700">
            <div class="flex-initial w-64">
                <SideBar />
            </div>
            <div class="flex-1 p-5 pt-20 ">
                <slot></slot>

                <!-- <h3>Footer</h3> -->
            </div>
            
        </div>
    </div>
</template>